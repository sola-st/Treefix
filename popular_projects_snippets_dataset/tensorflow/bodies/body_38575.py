# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/zero_division_test.py
with test_util.use_gpu():
    for dtype in dtypes.uint8, dtypes.int16, dtypes.int32, dtypes.int64:
        zero = constant_op.constant(0, dtype=dtype)
        one = constant_op.constant(1, dtype=dtype)
        bads = [lambda x, y: x // y]
        if dtype in (dtypes.int32, dtypes.int64):
            bads.append(lambda x, y: x % y)
        for bad in bads:
            try:
                result = self.evaluate(bad(one, zero))
            except (errors.OpError, errors.InvalidArgumentError) as e:
                # Ideally, we'd get a nice exception.  In theory, this should only
                # happen on CPU, but 32 bit integer GPU division is actually on
                # CPU due to a placer bug.
                # TODO(irving): Make stricter once the placer bug is fixed.
                self.assertIn('Integer division by zero', str(e))
            else:
                # On the GPU, integer division by zero produces all bits set.
                # But apparently on some GPUs "all bits set" for 64 bit division
                # means 32 bits set, so we allow 0xffffffff as well.  This isn't
                # very portable, so we may need to expand this list if other GPUs
                # do different things.
                #
                # XLA constant folds integer division by zero to 1.
                self.assertTrue(test.is_gpu_available())
                self.assertIn(result, (-1, 1, 2, 0xff, 0xffffffff))
