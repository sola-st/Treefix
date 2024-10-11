# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/utils_test.py
# Build a TensorInfo with name "bar/x:0".
with ops.Graph().as_default():
    with ops.name_scope("bar"):
        unscoped = array_ops.placeholder(dtypes.float32, 1, name="x")
        tensor_info = utils.build_tensor_info(unscoped)
        self.assertEqual("bar/x:0", tensor_info.name)
    # Build a graph with node "foo/bar/x:0", akin to importing into scope foo.
with ops.Graph().as_default():
    with ops.name_scope("foo"):
        with ops.name_scope("bar"):
            expected = array_ops.placeholder(dtypes.float32, 1, name="x")
    self.assertEqual("foo/bar/x:0", expected.name)
    # Test that tensor is found by prepending the import scope.
    actual = utils.get_tensor_from_tensor_info(tensor_info,
                                               import_scope="foo")
    self.assertEqual(expected.name, actual.name)
