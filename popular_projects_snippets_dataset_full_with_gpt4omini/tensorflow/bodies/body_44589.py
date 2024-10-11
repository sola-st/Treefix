# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
test_result = test()
try:
    # Note: Using try/except and not tensor_util.is_tf_type to avoid
    # performance degradation.
    exit(bool(test_result))
except errors_impl.OperatorNotAllowedInGraphError as e:
    ag_logging.log(
        1,
        'Caught error while evaluating while loop condition',
        exc_info=True)
    # TODO(mdan): distinguish beteen these two cases.
    raise NotImplementedError(
        'The condition of while loop started as non-Tensor, then changed to'
        ' Tensor. This may happen either because variables changed type, or'
        ' when a break or return statement inside the loop depends on a'
        ' Tensor condition. In both cases, changing to a TF loop should'
        ' remove the error.\nSee '
        'https://github.com/tensorflow/tensorflow/blob/master/tensorflow/'
        'python/autograph/g3doc/reference/limitations.md'
        '#consistency-of-control-flow-types for more info.') from e
