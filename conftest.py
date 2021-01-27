import os
from pytest_test_marker.manifest import ManifestFile
from pytest_test_marker.mark import CollectionModifier


default_mark_path = 'tests/test_data/marks.yml'

_mark_file_flag = '--mark-file'
_mark_file_opt = 'mark-file'

def pytest_addoption(parser):
    print("ADDING OPTION")
    parser.addoption(_mark_file_flag, dest=_mark_file_opt, type=str,
                     help='Path to file with mark definitions')


def add_custom_marks_to_pytest_config(config, marks):
    for marker in marks.keys():
        ini_line = "{}: generated by {}".format(marker,
                                                'pytest-test-marker')
        config.addinivalue_line('markers', ini_line)


def gather_marks(mark_file):
    if not mark_file:
        return {}
    manifest = ManifestFile(mark_file)
    return manifest.get_marks()


def apply_marks_to_collected_tests(items, marks):
    modifier = CollectionModifier(items, marks)
    modifier.apply_markers()


def pytest_collection_modifyitems(config, items):
    marks = gather_marks(config.getoption(_mark_file_opt))
    # Register marks with pytest before applying
    add_custom_marks_to_pytest_config(config, marks)
    apply_marks_to_collected_tests(items, marks)
