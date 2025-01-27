# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Testing name scope requires a graph.
with ops.Graph().as_default():
    x_shape = [13, 9, 3]
    x_np = np.ones(x_shape, dtype=np.float32)
    for use_gpu in [True, False]:
        with self.cached_session(use_gpu=use_gpu):
            y = image_ops.central_crop(x_np, 1.0)
            self.assertTrue(y.op.name.startswith("central_crop"))
