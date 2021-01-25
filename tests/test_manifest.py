import pytest

from pytest_test_marker.manifest import ManifestFile


test_yaml = 'tests/test_data/marks.yml'
test_json = 'tests/test_data/marks.json'


test_dict = {
    'example_marker': {
        'modules': ['src.test2'],
        'classes': ['src.test0.ExampleTestCase1'],
        'functions': ['src.test1.ExampleTestCase2.ex_test_func_2']
    }
}


def test_load_yaml_marks():
    manifest = ManifestFile(test_yaml)
    assert manifest.get_marks() == test_dict

def test_load_json_marks():
    manifest = ManifestFile(test_json)
    assert manifest.get_marks() == test_dict

def test_fd_closed():
    manifest = ManifestFile(test_yaml)
    fd = manifest.fd
    del manifest

    with pytest.raises(ValueError):
        fd.read()
