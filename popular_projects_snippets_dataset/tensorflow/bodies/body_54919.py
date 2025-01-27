# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/smart_cond_test.py
with ops.Graph().as_default():
    with session.Session():
        x = constant_op.constant(1)
        with self.assertRaises(TypeError):
            smart_cond.smart_cond(True, false_fn=lambda: x)
