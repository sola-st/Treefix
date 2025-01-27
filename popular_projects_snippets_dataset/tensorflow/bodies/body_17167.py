# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
if not context.executing_eagerly() and run_func_eagerly:
    # Skip running tf.function eagerly in V1 mode.
    self.skipTest("Skip test that runs tf.function eagerly in V1 mode.")
else:

    @def_function.function
    def test_dtype(image, target_shape, target_method):
        y = image_ops.resize_images_v2(image, target_shape, target_method)
        if method == image_ops.ResizeMethod.NEAREST_NEIGHBOR:
            expected_dtype = image.dtype
        else:
            expected_dtype = dtypes.float32

        self.assertEqual(y.dtype, expected_dtype)

    target_shapes = [[6, 4],
                     [3, 2],
                     [tensor_spec.TensorSpec(shape=None, dtype=dtypes.int32),
                      tensor_spec.TensorSpec(shape=None, dtype=dtypes.int32)]]

    for nptype in self.TYPES:
        image = tensor_spec.TensorSpec(shape=[1, 6, 4, 1], dtype=nptype)
        for method in self.METHODS:
            for target_shape in target_shapes:
                with test_util.run_functions_eagerly(run_func_eagerly):
                    test_dtype.get_concrete_function(image, target_shape, method)
