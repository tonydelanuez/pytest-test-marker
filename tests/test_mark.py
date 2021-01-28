import pytest
import uuid


from pytest_test_marker.mark import MarkDefinition, parse_nodeid


test_marker_name = 'example_marker'

test_dict = {
    test_marker_name: {
        'modules': ['src/test2.py'],
        'classes': ['src/test0.py::ExampleTestCase1'],
        'functions': ['src/test1.py::ExampleTestCase2::ex_test_func_2']
    }
}


def gen_test_id(include_class=True, include_func=True):
    testid = 'testdir/test_foo.py'
    if include_class:
        testid += '::TestClass'
    if include_func:
        testid += '::test_{}'.format(str(uuid.uuid4())[:8])
    return testid


def test_parse_nodeid_module_only():
    test_nodeid = "src/test.py"
    parsed = parse_nodeid(test_nodeid)

    assert parsed.module_path == "src/test.py"
    assert parsed.class_path is None
    assert parsed.func_path is None


def test_parse_nodeid_module_class():
    test_nodeid = "src/test.py::ExampleTestCase"

    parsed = parse_nodeid(test_nodeid)
    assert parsed.module_path == "src/test.py"
    assert parsed.class_path == "src/test.py::ExampleTestCase"
    assert parsed.func_path is None


def test_parse_nodeid_full_path():
    test_nodeid = "src/test.py::ExampleTestCase::test_foo"

    parsed = parse_nodeid(test_nodeid)
    assert parsed.module_path == "src/test.py"
    assert parsed.class_path == "src/test.py::ExampleTestCase"
    assert parsed.func_path == "src/test.py::ExampleTestCase::test_foo"


@pytest.mark.parametrize("test_path,expected",
                         [("src/test2.py", True),
                          ("src/WRONG.py", False)])
def test_markdefinition_in_marked_module(test_path, expected):
    md = MarkDefinition(test_marker_name, test_dict[test_marker_name])
    assert md.in_marked_module(test_path) == expected


@pytest.mark.parametrize("test_path,expected",
                         [("src/test0.py::ExampleTestCase1", True),
                          ("src/test2.py::UnmarkedTestCase", False)])
def test_markdefinition_in_marked_class(test_path, expected):
    md = MarkDefinition(test_marker_name, test_dict[test_marker_name])
    assert md.in_marked_class(test_path) == expected


@pytest.mark.parametrize("test_path,expected",
                         [("src/test1.py::ExampleTestCase2::ex_test_func_2", True),
                          ("src/test2.py::UnmarkedTestCase::test_foo", False)])
def test_markdefinition_in_marked_function(test_path, expected):
    md = MarkDefinition(test_marker_name, test_dict[test_marker_name])
    assert md.in_marked_func(test_path) == expected
