# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
with ops.Graph().as_default():
    pred = array_ops.placeholder(dtypes.bool, name="pred")
    x = constant_op.constant(3.0, name="x")
    ops.add_to_collection("x", x)

    def true_fn():
        exit(math_ops.pow(x, 3))

    def false_fn():
        exit(x)

    ops.add_to_collection("pred", pred)
    cond = cond_v2.cond_v2(pred, true_fn, false_fn, name="cond")
    ops.add_to_collection("cond", cond)
    meta_graph = saver.export_meta_graph()

with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        saver.import_meta_graph(meta_graph)
        x = ops.get_collection("x")[0]
        pred = ops.get_collection("pred")[0]
        cond = ops.get_collection("cond")
        cond_grad = gradients_impl.gradients(cond, [x], name="cond_grad")
        cond_grad_grad = gradients_impl.gradients(
            cond_grad, [x], name="cond_grad_grad")
        # d[x^3]/dx = 3x^2
        true_val = sess.run(cond_grad, {pred: True})
        self.assertEqual(true_val, [27.0])
        # d[x]/dx = 1
        false_val = sess.run(cond_grad, {pred: False})
        self.assertEqual(false_val, [1.0])

        true_val = sess.run(cond_grad_grad, {pred: True})
        # d2[x^3]/dx2 = 6x
        self.assertEqual(true_val, [18.0])
        false_val = sess.run(cond_grad_grad, {pred: False})
        # d2[x]/dx2 = 0
        self.assertEqual(false_val, [0.0])
