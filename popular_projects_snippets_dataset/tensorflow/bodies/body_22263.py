# Extracted from ./data/repos/tensorflow/tensorflow/python/training/quantize_training_test.py
with session.Session() as sess:
    a = constant_op.constant(6.0, shape=[1, 1])
    b = constant_op.constant(7.0, shape=[1, 1])
    c = math_ops.matmul(a, b, name='matmul')

    self.assertEqual(c.eval(), 42.0)
    self.assertEqual(len(sess.graph_def.node), 3)

    result = quantize_training.do_quantize_training_on_graphdef(
        sess.graph_def, 8)

    # We just want to guarantee that some rewrite happened.
    self.assertGreater(len(result.node), 3)
