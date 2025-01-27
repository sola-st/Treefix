# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/conditional_accumulator_test.py
q = data_flow_ops.ConditionalAccumulator(
    dtypes_lib.float32, name="Q", shape=(3, 2))

with self.assertRaises(ValueError):
    q.apply_grad([[1.0, 2.0], [3.0, 4.0]])

with self.assertRaises(ValueError):
    q.apply_grad([[1.0], [2.0], [3.0]])
