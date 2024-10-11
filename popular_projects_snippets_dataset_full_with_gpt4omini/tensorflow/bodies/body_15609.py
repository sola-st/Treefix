# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_range_op_test.py
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            r'Requires delta != 0'):
    self.evaluate(ragged_math_ops.range(0, 0, 0))

with self.assertRaisesRegex(errors.InvalidArgumentError,
                            r'Requires \(\(limit - start\) / delta\) <='):
    self.evaluate(ragged_math_ops.range(0.1, 1e10, 1e-10))

with self.assertRaisesRegex(errors.InvalidArgumentError, 'overflowed'):
    self.evaluate(
        gen_ragged_math_ops.ragged_range(
            starts=[0, 0],
            limits=[2**31 - 1, 1],
            deltas=[1, 1],
            Tsplits=dtypes.int32))
