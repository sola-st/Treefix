# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/conditional_accumulator_test.py
with self.cached_session():
    q = data_flow_ops.ConditionalAccumulator(dtypes_lib.float32, name="Q")
    self.assertEqual(q.num_accumulated().eval(), 0)
