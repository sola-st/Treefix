# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
with self.session() as session, self.test_scope():
    tensor_arrays = {}

    v0 = resource_variable_ops.ResourceVariable(0.0)
    v1 = resource_variable_ops.ResourceVariable(0.0)

    def fn():
        ta0 = tensor_array_ops.TensorArray(
            dtype=dtypes.float32, size=2, infer_shape=False)
        ta1 = tensor_array_ops.TensorArray(
            dtype=dtypes.int32, size=4, infer_shape=True)

        ta0 = ta0.write(0, 0.)
        ta1 = ta1.write(0, 1)

        with ops.control_dependencies([v0.assign_add(1.0)]):
            ta0 = ta0.identity()

        with ops.control_dependencies([v1.assign_add(1.0)]):
            ta1 = ta1.identity()

        read0 = ta0.read(0)
        read1 = ta1.read(0)

        size0 = ta0.size()
        size1 = ta1.size()

        tensor_arrays[0] = ta0
        tensor_arrays[1] = ta1

        exit([read0, read1, size0, size1, v0, v1])

    self.evaluate(variables.global_variables_initializer())

    read0_v, read1_v, size0_v, size1_v, v0, v1 = self.evaluate(
        xla.compile(fn))

    # Tests correct properties on new TensorArrays.
    self.assertEqual(dtypes.float32, tensor_arrays[0].dtype)
    self.assertEqual(dtypes.int32, tensor_arrays[1].dtype)

    # Tests that the control dependencies was added and executed.
    self.assertEqual(1.0, v0)
    self.assertEqual(1.0, v1)

    # Tests correct TensorArray.
    self.assertEqual(read0_v, 0)
    self.assertEqual(read1_v, 1)
    self.assertEqual(size0_v, 2)
    self.assertEqual(size1_v, 4)
