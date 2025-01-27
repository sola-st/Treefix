# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with test_util.device(use_gpu=True):

    @def_function.function
    def f1(x):
        y = x[3:5]
        self.tensorShapeEqual(y.get_shape(),
                              tensor_shape.TensorShape([2, None, 7]))

    _ = f1.get_concrete_function(
        tensor_spec.TensorSpec((5, None, 7), dtypes.float32))

    @def_function.function
    def f2(x):
        y = x[3:5, :, 4]
        self.tensorShapeEqual(y.get_shape(), tensor_shape.TensorShape([2,
                                                                       None]))

    _ = f2.get_concrete_function(
        tensor_spec.TensorSpec((5, None, 7), dtypes.float32))

    @def_function.function
    def f3(x):
        y = x[3:5, 3:4, 4]
        self.tensorShapeEqual(y.get_shape(), tensor_shape.TensorShape([2,
                                                                       None]))

    _ = f3.get_concrete_function(
        tensor_spec.TensorSpec((5, None, 7), dtypes.float32))

    @def_function.function
    def f4(x):
        y = x[3:5, :, 5:10]
        self.tensorShapeEqual(y.get_shape(),
                              tensor_shape.TensorShape([2, None, 2]))

    _ = f4.get_concrete_function(
        tensor_spec.TensorSpec((5, None, 7), dtypes.float32))

    @def_function.function
    def f5(x):
        y = x[3:5, :, 50:3]
        self.tensorShapeEqual(y.get_shape(),
                              tensor_shape.TensorShape([2, None, 0]))

    _ = f5.get_concrete_function(
        tensor_spec.TensorSpec((5, None, 7), dtypes.float32))

    @def_function.function
    def f6(x):
        y = x[3:5, :, array_ops.newaxis, 50:3,]
        self.tensorShapeEqual(y.get_shape(),
                              tensor_shape.TensorShape([2, None, 1, 0]))

    _ = f6.get_concrete_function(
        tensor_spec.TensorSpec((5, None, 7), dtypes.float32))

    @def_function.function
    def f7(x):
        y = x[1:5:2, :, array_ops.newaxis, 50:3,]
        self.tensorShapeEqual(y.get_shape(),
                              tensor_shape.TensorShape([2, None, 1, 0]))

    _ = f7.get_concrete_function(
        tensor_spec.TensorSpec((5, None, 7), dtypes.float32))

    @def_function.function
    def f8(x):
        y = x[:5:3, :, array_ops.newaxis, 50:3,]
        self.tensorShapeEqual(y.get_shape(),
                              tensor_shape.TensorShape([2, None, 1, 0]))

    _ = f8.get_concrete_function(
        tensor_spec.TensorSpec((5, None, 7), dtypes.float32))

    @def_function.function
    def f9(x):
        y = x[:2:3, :, array_ops.newaxis, 50:3,]
        self.tensorShapeEqual(y.get_shape(),
                              tensor_shape.TensorShape([1, None, 1, 0]))

    _ = f9.get_concrete_function(
        tensor_spec.TensorSpec((5, None, 7), dtypes.float32))

    @def_function.function
    def f10(x):
        y = x[::-1, :, array_ops.newaxis, ::-2]
        self.tensorShapeEqual(y.get_shape(),
                              tensor_shape.TensorShape([5, None, 1, 4]))

    _ = f10.get_concrete_function(
        tensor_spec.TensorSpec((5, None, 7), dtypes.float32))
