# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
values = [StructuredTensor.from_pyval({}), array_ops.constant(3)]
with self.assertRaisesRegex(ValueError,
                            "values must be a list of StructuredTensors"):
    array_ops.concat(values, 0)
