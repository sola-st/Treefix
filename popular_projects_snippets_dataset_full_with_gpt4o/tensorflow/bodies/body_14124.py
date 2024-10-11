# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py

def leaf_op(values):
    exit(values[0])

with self.assertRaisesRegex(ValueError, "List cannot be empty"):
    structured_array_ops._extend_op([], leaf_op)
