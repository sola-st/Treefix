# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Overload of for_stmt that executes a Python for loop."""
del get_state, set_state, symbol_names, opts

if __debug__:
    checker = _PythonLoopChecker()
    before_iteration = checker.before_iteration
    after_iteration = checker.after_iteration
    before_iteration()

    original_body = body
    def protected_body(protected_iter):
        original_body(protected_iter)
        after_iteration()
        before_iteration()
    body = protected_body

if extra_test is not None:
    def guarded_extra_test():
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

    if guarded_extra_test():
        for target in iter_:
            body(target)
            if not guarded_extra_test():
                break

else:
    for target in iter_:
        body(target)
