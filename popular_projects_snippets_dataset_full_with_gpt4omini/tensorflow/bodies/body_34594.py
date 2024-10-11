# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session():
    ta0 = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=2,
                                       infer_shape=False)
    ta1 = tensor_array_ops.TensorArray(dtype=dtypes.int32, size=4,
                                       infer_shape=True)

    ta0 = ta0.write(0, 0.)
    ta1 = ta1.write(0, 1)

    v0 = variable_scope.get_variable(
        "v0", shape=(), initializer=init_ops.zeros_initializer())
    v1 = variable_scope.get_variable(
        "v1", shape=(), initializer=init_ops.zeros_initializer())

    with ops.control_dependencies([v0.assign_add(1)]):
        ta0 = ta0.identity()

    with ops.control_dependencies([v1.assign_add(1)]):
        ta1 = ta1.identity()

    read0 = ta0.read(0)
    read1 = ta1.read(0)

    size0 = ta0.size()
    size1 = ta1.size()

    # Tests correct properties on new TensorArrays.
    self.assertEqual(dtypes.float32, ta0.dtype)
    self.assertEqual(dtypes.int32, ta1.dtype)
    if context.executing_eagerly():
        self.assertEqual(tensor_shape.TensorShape([]), read0.get_shape())
    else:
        self.assertEqual(tensor_shape.unknown_shape(), read0.get_shape())
    self.assertEqual(tensor_shape.TensorShape([]), read1.get_shape())

    if not context.executing_eagerly():
        self.evaluate(variables.global_variables_initializer())

    read0_v, read1_v, size0_v, size1_v = self.evaluate((read0, read1, size0,
                                                        size1))

    # Tests that the control dependencies was added and executed.
    self.assertEqual(1, self.evaluate(v0))
    self.assertEqual(1, self.evaluate(v1))

    # Tests correct TensorArray.
    self.assertEqual(read0_v, 0)
    self.assertEqual(read1_v, 1)
    self.assertEqual(size0_v, 2)
    self.assertEqual(size1_v, 4)
