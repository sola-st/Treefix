# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
with ops.Graph().as_default():
    with self.assertRaises(ValueError):
        data_flow_ops.SparseConditionalAccumulator(
            dtypes_lib.float32, name="Q", reduction_type="Invalid")
