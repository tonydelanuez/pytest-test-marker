import os

pytest_plugins = ['pytester']

def test_mypytest_test(testdir):
    pytestfile = testdir.makepyfile("""
        def test_x(): pass
        def test_y(): pass
        def test_z(): pass
    """)
    markfile = testdir.makefile('.yml', """
    example_mark:
        functions:
            {}::test_x
    """.format(str(pytestfile)))

    result = testdir.runpytest_subprocess('--mark-file', str(markfile))
    result.assert_outcomes(passed=1)
