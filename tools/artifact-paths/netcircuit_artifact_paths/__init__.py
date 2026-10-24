"""Python bridge to the single Node artifact path/ownership implementation."""
import os
import json
from pathlib import Path
import shutil
import subprocess

_CLI = Path(__file__).resolve().with_name('artifact-paths.mjs')


def _invoke(*arguments, environment=None):
    node = shutil.which('node')
    if not node:
        raise RuntimeError('Node is required by the shared artifact allocator; no repository fallback is allowed.')
    try:
        result = subprocess.run([node, str(_CLI), *map(str, arguments)], capture_output=True, text=True, check=True, env=environment)
    except subprocess.CalledProcessError as error:
        raise RuntimeError(error.stderr.strip() or 'Artifact allocator failed; no repository fallback is allowed.') from error
    return result.stdout.strip()


def _context_arguments(context):
    return ['--context', json.dumps(context)] if context is not None else []


def artifact_context(context=None):
    """Resolve context through Node; never infer roots independently in Python."""
    return json.loads(_invoke('--context-info', *_context_arguments(context)))


def artifact_directory(subdirectory='', directory=None, *, context=None):
    selected = artifact_context(context)
    arguments = ['--directory', directory] if directory is not None else []
    arguments.extend(_context_arguments(selected))
    # A separate CLI process cannot export its environment to Python: inherit the
    # allocated root explicitly so backend subprocesses reuse this exact session.
    session = Path(_invoke(*arguments))
    environment = {**os.environ, 'NETCIRCUIT_ARTIFACTS_SESSION': str(session),
                   'NETCIRCUIT_ARTIFACTS_CONTEXT': json.dumps(selected)}
    result = Path(_invoke(subdirectory, environment=environment)) if subdirectory else session
    if directory is None:
        os.environ['NETCIRCUIT_ARTIFACTS_SESSION'] = str(session)
        os.environ['NETCIRCUIT_ARTIFACTS_CONTEXT'] = json.dumps(selected)
    return result


def validate_artifact_directory(directory, *, context=None):
    return Path(_invoke('--validate', directory, *_context_arguments(context)))


def cleanup_artifact_session(directory, *, context=None):
    _invoke('--cleanup', directory, *_context_arguments(context))
    if os.environ.get('NETCIRCUIT_ARTIFACTS_SESSION') == str(directory):
        os.environ.pop('NETCIRCUIT_ARTIFACTS_SESSION', None)
