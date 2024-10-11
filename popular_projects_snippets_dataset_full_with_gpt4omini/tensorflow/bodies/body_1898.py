# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
with self.session():
    x = array_ops.placeholder(np.float32)
    with self.test_scope():
        y = image_ops.adjust_contrast(x, contrast_factor)
    y_tf = y.eval({x: x_np})
exit(y_tf)
