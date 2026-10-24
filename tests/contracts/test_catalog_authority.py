"""One editable Device Library, with generated installed resource projections."""
import json
from pathlib import Path
import shutil
import sys

import pytest

from contracts.codegen import sync_editor_catalog as catalog

ROOT = Path(__file__).resolve().parents[2]


def checkout(tmp_path, monkeypatch, *, source=True):
    shutil.copytree(ROOT/'contracts', tmp_path/'contracts')
    if source:
        shutil.copytree(ROOT/'device-library', tmp_path/'device-library')
    monkeypatch.setattr(catalog, 'ROOT', tmp_path)
    return tmp_path


def change_name(path):
    data = json.loads(path.read_text(encoding='utf-8'))
    data['components'][0]['name'] += ' changed in canonical source'
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    return data['components'][0]['name']


def test_source_check_detects_canonical_edit_even_with_old_packaged_mirror(tmp_path, monkeypatch):
    checkout(tmp_path, monkeypatch)
    change_name(tmp_path/'device-library/editor/components.json')
    monkeypatch.setattr(sys, 'argv', ['sync_editor_catalog', '--check'])
    with pytest.raises(SystemExit, match='[Ss]tale'):
        catalog.main()


def test_source_generation_updates_mirror_and_browser_from_one_input(tmp_path, monkeypatch):
    checkout(tmp_path, monkeypatch)
    expected = change_name(tmp_path/'device-library/editor/components.json')
    monkeypatch.setattr(sys, 'argv', ['sync_editor_catalog'])
    catalog.main()
    for path in ('contracts/catalog-source/editor/components.json', 'contracts/browser/data/editorCatalog.json'):
        assert json.loads((tmp_path/path).read_text(encoding='utf-8'))['components'][0]['name'] == expected
    monkeypatch.setattr(sys, 'argv', ['sync_editor_catalog', '--check'])
    catalog.main()


def test_installed_mode_reads_packaged_inputs_without_source_directory(tmp_path, monkeypatch):
    checkout(tmp_path, monkeypatch, source=False)
    monkeypatch.setattr(sys, 'argv', ['sync_editor_catalog', '--check'])
    catalog.main()
    assert not (tmp_path/'device-library').exists()


def test_unified_generation_checks_catalog_outputs_as_part_of_the_same_set(tmp_path, monkeypatch):
    from contracts.codegen import generate_contracts as generator
    checkout(tmp_path, monkeypatch)
    expected = change_name(tmp_path/'device-library/editor/components.json')
    monkeypatch.setattr(generator, 'ROOT', tmp_path)
    output = tmp_path/'result'
    generator.generate(output_root=output, node_tools=ROOT/'packages/public-sdk')
    assert json.loads((output/'contracts/browser/data/editorCatalog.json').read_text(encoding='utf-8'))['components'][0]['name'] == expected
    assert (output/'contracts/catalog-source/editor/components.json').read_bytes().replace(b'\r\n', b'\n') == (tmp_path/'device-library/editor/components.json').read_bytes().replace(b'\r\n', b'\n')
