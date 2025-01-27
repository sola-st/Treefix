# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with self.cached_session():
    x = constant_op.constant(x_np)
    y = image_ops.adjust_hue(x, delta_h)
    y_tf = self.evaluate(y)
exit(y_tf)
