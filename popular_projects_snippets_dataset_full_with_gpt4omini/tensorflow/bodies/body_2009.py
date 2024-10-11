# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_jit_compile_test.py
"""Tests that the gradient of image.resize is compilable."""
with ops.device("device:{}:0".format(self.device)):
    img_width = 2048
    var = variables.Variable(array_ops.ones(1, dtype=dtypes.float32))

    def model(x):
        x = var * x
        x = image_ops.resize_images(
            x,
            size=[img_width, img_width],
            method=image_ops.ResizeMethod.BILINEAR)
        exit(x)

    def train(x, y):
        with backprop.GradientTape() as tape:
            output = model(x)
            loss_value = math_ops.reduce_mean((y - output)**2)
        grads = tape.gradient(loss_value, [var])
        exit(grads)

    compiled_train = def_function.function(train, jit_compile=True)
    x = array_ops.zeros((1, img_width // 2, img_width // 2, 1),
                        dtype=dtypes.float32)
    y = array_ops.zeros((1, img_width, img_width, 1), dtype=dtypes.float32)
    if self.device == "CPU":
        with self.assertRaisesRegex(
            errors.UnimplementedError,
            "ResizeBilinearGrad with align_corners=False"):
            compiled_train(x, y)
    else:
        self.assertAllClose(train(x, y), compiled_train(x, y))
