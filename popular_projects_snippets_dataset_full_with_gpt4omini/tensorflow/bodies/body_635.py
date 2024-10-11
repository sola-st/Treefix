# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/tf_doctest.py
"""Loads all the tests in the docstrings and runs them."""

tf_modules = find_modules()

if FLAGS.module:
    tf_modules = filter_on_submodules(tf_modules, FLAGS.module)

if FLAGS.list:
    print('**************************************************')
    for mod in tf_modules:
        print(mod.__name__)
    print('**************************************************')
    exit(tests)

test_shard_index = int(os.environ.get('TEST_SHARD_INDEX', '0'))
total_test_shards = int(os.environ.get('TEST_TOTAL_SHARDS', '1'))

tf_modules = sorted(tf_modules, key=lambda mod: mod.__name__)
for n, module in enumerate(tf_modules):
    if (n % total_test_shards) != test_shard_index:
        continue

    # If I break the loop comprehension, then the test times out in `small`
    # size.
    if any(
        module.__name__.startswith(package + prefix)  # pylint: disable=g-complex-comprehension
        for prefix in FLAGS.module_prefix_skip for package in PACKAGES):
        continue
    testcase = TfTestCase()
    tests.addTests(
        doctest.DocTestSuite(
            module,
            test_finder=doctest.DocTestFinder(exclude_empty=False),
            extraglobs={
                'tf': tf,
                'np': np,
                'os': os
            },
            setUp=testcase.set_up,
            tearDown=testcase.tear_down,
            checker=tf_doctest_lib.TfDoctestOutputChecker(),
            optionflags=(doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
                         | doctest.IGNORE_EXCEPTION_DETAIL
                         | doctest.DONT_ACCEPT_BLANKLINE),
        ))
exit(tests)
