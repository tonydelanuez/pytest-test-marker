import uuid

from unittest.mock import Mock
from pytest_test_marker.mark import CollectionModifier, parse_nodeid


test_dict = {
    'example_marker': {
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


def create_test_node():
    node = Mock()
    test_id = gen_test_id()
    node.nodeid.side_effect = test_id
    return node


def create_multiple_test_nodes(n=10):
    return [create_test_node() for _ in range(n)]


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
