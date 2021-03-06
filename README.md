# pytest-test-marker

This package gives you the ability to define your pytest markers in a configuration file
via YAML/JSON. You can use this tool to mark individual test functions, classes, or entire modules
with a custom pytest marker.

Rather than wrapping individual functions or classes with the @pytest.mark.foo decorator, declare your
markers alongside of your code for easy updating / keeping track of large lists of markers.

*pytest-test-marker is tested on Python 2.7, 3.6, 3.7, 3.8, and 3.9*

## Usage:

Declare a pytest marker file in either YAML or JSON

pytest_markers.yaml:
```
example_marker:
    modules:
        - src / test2.py
    classes:
        - src/test0.py::ExampleTestCase1
    functions:
        - src/test1.py::ExampleTestCase2::ex_test_func_2
        - tests/test_mark.py::test_collection_modifier_init_markdefs
```

pytest_markers.json:
```
{
    "example_marker": {
        "modules": [
            "src/test2.py"
        ],
        "classes": [
            "src/test0.py::ExampleTestCase1"
        ],
        "functions": [
            "src/test1.py::ExampleTestCase2::ex_test_func_2"
        ]
    }
}
```

Install the plugin: 
`pip install pytest-test-marker`

When invoking pytest, use the `--mark-file` option (as well as any markers you want checked in your test run):
`pytest /path/to/tests --mark-file pytest_markers.yml` 


