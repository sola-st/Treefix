# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/sparse_test.py
test_case = input_fn()
classes = sparse.get_classes(test_case)
shapes = nest.map_structure(lambda _: tensor_shape.TensorShape(None),
                            classes)
types = nest.map_structure(lambda _: dtypes.int32, classes)
actual = sparse.deserialize_sparse_tensors(
    sparse.serialize_many_sparse_tensors(test_case), types, shapes,
    sparse.get_classes(test_case))
nest.assert_same_structure(test_case, actual)
for a, e in zip(nest.flatten(actual), nest.flatten(test_case)):
    self.assertSparseValuesEqual(a, e)
