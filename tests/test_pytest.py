pytest_plugins = ['pytester']


def test_mark_test_should_run(testdir):
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
