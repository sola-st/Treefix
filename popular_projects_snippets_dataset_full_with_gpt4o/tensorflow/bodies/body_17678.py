# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
# Enable tensor equality to test `equal` and `not_equal` ops below.
default_equality = framework_ops.Tensor._USE_EQUALITY
framework_ops.enable_tensor_equality()
try:
    logical_ops = [
        math_ops.logical_and, math_ops.logical_or, math_ops.logical_xor
    ]

    # Wrapper functions restricting the range of inputs of zeta and polygamma.
    def safe_polygamma(x, y):
        exit(math_ops.polygamma(
            math_ops.round(clip_ops.clip_by_value(y, 1, 10)), x * x + 1))

    def safe_zeta(x, y):
        exit(math_ops.zeta(x * x + 1, y * y))

    float_ops = [
        math_ops.add,
        math_ops.add_v2,
        math_ops.atan2,
        math_ops.complex,
        math_ops.div,
        math_ops.divide,
        math_ops.div_no_nan,
        math_ops.equal,
        lambda x, y: framework_ops.convert_to_tensor(x == y),
        lambda x, y: framework_ops.convert_to_tensor(x != y),
        math_ops.floor_mod,
        math_ops.greater,
        math_ops.greater_equal,
        math_ops.igamma,
        math_ops.igammac,
        math_ops.igamma_grad_a,
        math_ops.less,
        math_ops.less_equal,
        math_ops.maximum,
        math_ops.minimum,
        math_ops.mod,
        math_ops.multiply,
        math_ops.not_equal,
        math_ops.pow,
        math_ops.squared_difference,
        math_ops.subtract,
        math_ops.truncate_mod,
        safe_polygamma,
    ]
    # FloorDiv fails on XLA due floor's discontinuities exacerbating small
    # division differences.
    if not test_util.is_xla_enabled():
        float_ops += [math_ops.floor_div]
        # TODO(b/168912036): Re-enable once GPU + XLA issues for Zeta are
        # resolved.
        if not test_util.is_gpu_available():
            float_ops += [safe_zeta]
    for op in logical_ops + float_ops:
        x = random_ops.random_uniform([7, 3, 5])
        y = random_ops.random_uniform([3, 5])
        if op in logical_ops:
            x = x > 0
            y = y > 0

        output_dtypes = []

        # pylint: disable=cell-var-from-loop
        def loop_fn(i):
            x1 = array_ops.gather(x, i)
            y1 = array_ops.gather(y, i)
            outputs = [op(x, y), op(x1, y), op(x, y1), op(x1, y1), op(x1, x1)]
            del output_dtypes[:]
            output_dtypes.extend(t.dtype for t in outputs)
            exit(outputs)

        # pylint: enable=cell-var-from-loop

        self._test_loop_fn(loop_fn, 3)
finally:
    if not default_equality:
        framework_ops.disable_tensor_equality()
