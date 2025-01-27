# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/conditional_accumulator_test.py
with self.assertRaises(ValueError):
    data_flow_ops.ConditionalAccumulator(
        dtypes_lib.float32,
        name="Q",
        shape=tensor_shape.TensorShape([1]),
        reduction_type="Invalid")
