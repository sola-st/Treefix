# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
with self.cached_session():
    q = data_flow_ops.SparseConditionalAccumulator(
        dtypes_lib.float32, name="Q")
    self.assertEqual(q.num_accumulated().eval(), 0)
