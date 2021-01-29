pytest_plugins = ['pytester']


def test_mark_func_should_run(testdir):
    pytestfile = testdir.makepyfile("""
        def test_x(): pass
        def test_y(): pass
        def test_z(): pass
    """)

    markfile = testdir.makefile('.yml', """
    example_mark:
        functions:
            - {}::test_x
    """.format(pytestfile.basename))

    result = testdir.runpytest('--mark-file',
                               str(markfile),
                               '-m',
                               'example_mark')
    result.assert_outcomes(passed=1)


def test_mark_class_should_run(testdir):
    pytestfile = testdir.makepyfile("""

    def test_x(): pass

    class TestFoo:
        def test_y(self): pass

        def test_z(self): pass

    """)

    markfile = testdir.makefile('.yml', """
    example_mark:
        classes:
            - {}::TestFoo
    """.format(pytestfile.basename))

    result = testdir.runpytest('--mark-file',
                               str(markfile),
                               '-m',
                               'example_mark')
    result.assert_outcomes(passed=2)


def test_mark_module_should_run(testdir):
    pytestfile = testdir.makepyfile("""
        def test_x(): pass
        def test_y(): pass
        def test_z(): pass
    """)
    testdir.makepyfile("""
        def test_x(): pass
        def test_y(): pass
        def test_z(): pass
    """)

    markfile = testdir.makefile('.yml', """
    example_mark:
        modules:
            - {}
    """.format(pytestfile.basename))

    result = testdir.runpytest('--mark-file',
                               str(markfile),
                               '-m',
                               'example_mark')
    result.assert_outcomes(passed=3)
