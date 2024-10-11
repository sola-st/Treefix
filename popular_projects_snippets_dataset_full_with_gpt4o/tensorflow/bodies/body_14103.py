# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
st = [[[{"x": [1]}, {"x": [2]}], [{"x": [3]}]], [[{"x": [4, 5]}]]]
st = StructuredTensor.from_pyval(st)
with self.assertRaisesRegex(ValueError,
                            "axis=-5 out of bounds: expected -4<=axis<4"):
    array_ops.expand_dims(st, -5)
