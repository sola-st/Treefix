# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with self.session():

    @def_function.function
    def f1(x, y):
        z = x[y]
        self.tensorShapeEqual(z.get_shape(), tensor_shape.TensorShape([3, 7]))

    _ = f1.get_concrete_function(
        tensor_spec.TensorSpec((5, 3, 7)),
        tensor_spec.TensorSpec((), dtypes.int32))

    @def_function.function
    def f2(x, y):
        z = x[y, ::-1]
        self.tensorShapeEqual(z.get_shape(), tensor_shape.TensorShape([3, 7]))

    _ = f2.get_concrete_function(
        tensor_spec.TensorSpec((5, 3, 7)),
        tensor_spec.TensorSpec((), dtypes.int32))

    @def_function.function
    def f3(x, y):
        z = x[y, ::-2]
        self.tensorShapeEqual(z.get_shape(), tensor_shape.TensorShape([2, 7]))

    _ = f3.get_concrete_function(
        tensor_spec.TensorSpec((5, 3, 7)),
        tensor_spec.TensorSpec((), dtypes.int32))

    @def_function.function
    def f4(x, y, s):
        z = x[y, s:2]
        self.tensorShapeEqual(z.get_shape(), tensor_shape.TensorShape([None,
                                                                       7]))

    _ = f4.get_concrete_function(
        tensor_spec.TensorSpec((5, 3, 7)),
        tensor_spec.TensorSpec((), dtypes.int32),
        tensor_spec.TensorSpec((), dtypes.int32))
