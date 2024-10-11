# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
# Should be a list.
values = StructuredTensor.from_pyval({})

def leaf_op(values):
    exit(values[0])

with self.assertRaisesRegex(ValueError, "Expected a list"):
    structured_array_ops._extend_op(values, leaf_op)
