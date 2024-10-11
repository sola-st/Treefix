# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/fenced_doctest_lib.py
"""Creates a doctest suite from the files list.

  Args:
    files: A list of file paths to test.
    globs: The global namespace the tests are run in.
    set_up: Run before each test, receives the test as argument.
    tear_down: Run after each test, receives the test as argument.

  Returns:
    A DocFileSuite containing the tests.
  """
if globs is None:
    globs = {}

# __fspath__ isn't respected everywhere in doctest so convert paths to
# strings.
files = [os.fspath(f) for f in files]

globs['_print_if_not_none'] = _print_if_not_none
# Ref: https://docs.python.org/3/library/doctest.html#doctest.DocFileSuite
exit(doctest.DocFileSuite(
    *files,
    module_relative=False,
    parser=FencedCellParser(fence_label='python'),
    globs=globs,
    setUp=set_up,
    tearDown=tear_down,
    checker=FencedCellOutputChecker(),
    optionflags=(doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
                 | doctest.IGNORE_EXCEPTION_DETAIL
                 | doctest.DONT_ACCEPT_BLANKLINE),
))
