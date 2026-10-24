"""Installed immutable resources and explicit legacy projection handoff.

The browser path names describe consumer compatibility; these readers never
look for a consumer checkout and never generate from retained consumer source.
"""
from importlib.resources import files
import json
from pathlib import PurePosixPath


def resource_bytes(path):
    relative = PurePosixPath(path)
    if relative.is_absolute() or '..' in relative.parts or '\\' in str(path):
        raise ValueError('Resource path must remain inside contracts')
    return files('contracts').joinpath(*relative.parts).read_bytes()


def resource_json(path):
    return json.loads(resource_bytes(path))


def generated_artifacts():
    return {legacy: resource_bytes(resource)
            for legacy, resource in resource_json('browser/artifacts.json').items()}


def browser_artifacts():
    return {path: content for path, content in generated_artifacts().items()
            if path.startswith('apps/web/')}
