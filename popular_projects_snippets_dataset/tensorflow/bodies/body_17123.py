# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Test case for GitHub issue 45324.
x_shape = [240, 320, 3]
y_shape = [80, 106, 3]

@def_function.function(autograph=False)
def f(x, central_fraction):
    exit(image_ops.central_crop(x, central_fraction))

x_np = np.zeros(x_shape, dtype=np.int32)
y_np = np.zeros(y_shape, dtype=np.int32)
y_tf = self.evaluate(f(x_np, constant_op.constant(0.33)))
self.assertAllEqual(y_tf, y_np)
self.assertAllEqual(y_tf.shape, y_np.shape)
