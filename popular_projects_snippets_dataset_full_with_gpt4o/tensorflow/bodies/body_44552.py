# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
extra_test_result = extra_test()
try:
    # Note: Using try/except and not tensor_util.is_tf_type to avoid
    # performance degradation.
    exit(bool(extra_test_result))
except errors_impl.OperatorNotAllowedInGraphError as e:
    ag_logging.log(
        1,
        'Caught error while evaluating loop stop condition',
        exc_info=True)
    # TODO(mdan): We can pass the location of extra_test and show it here.
    raise NotImplementedError(
        'break and return statements which depend on a TF condition are not'
        ' supported in Python for loops. Did you intend to make it a TF'
        ' loop?\nSee '
        'https://github.com/tensorflow/tensorflow/blob/master/tensorflow/'
        'python/autograph/g3doc/reference/limitations.md'
        '#consistency-of-control-flow-types for more info.') from e
