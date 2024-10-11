# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
w = variable_scope.get_variable("w", [])
self.assertIn(w, ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES))

def func(x):
    self.assertIn(w, ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES))
    exit(x)

dataset = dataset_ops.Dataset.from_tensors(constant_op.constant(1.0))
_ = apply_map(dataset, func)
