# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
with self.assertRaisesRegex(
    TypeError, "Could not build a structure for output class "
    "_EagerTensorArray. Make sure any component class in "
    "`output_classes` inherits from one of the following classes: "
    "`tf.TypeSpec`, `tf.sparse.SparseTensor`, `tf.Tensor`, "
    "`tf.TensorArray`."):
    structure.convert_legacy_structure(dtypes.int32,
                                       tensor_shape.TensorShape([2, None]),
                                       tensor_array_ops._EagerTensorArray)
