# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
with self.session():
    x = array_ops.placeholder(dtypes.float32)
    with self.test_scope():
        y = gen_image_ops.adjust_hue(x, delta_h)
    y_tf = y.eval({x: x_np})
exit(y_tf)
