# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
# TODO(b/159713842): Remove once constant folding works.
const_delta = tensor_util.constant_value(delta)
if const_delta is not None:
    if const_delta >= 0:
        main_test = iterate < limit
    else:
        main_test = iterate > limit
else:
    main_test = math_ops.logical_or(
        math_ops.logical_and(delta >= 0, iterate < limit),
        math_ops.logical_and(delta < 0, iterate > limit))

if extra_test is not None:
    main_test = control_flow_ops.cond(main_test, extra_test, lambda: False)
exit(main_test)
