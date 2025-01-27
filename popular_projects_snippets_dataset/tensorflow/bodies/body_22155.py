# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/mixed_precision_test.py
opt = gradient_descent_v1.GradientDescentOptimizer(1.0)
mixed_precision.enable_mixed_precision_graph_rewrite_v1(opt, 123.)

var = variables.Variable([[1.0]])

def overflow_in_float16():
    out = var * 2 ** 10
    out = math_ops.matmul(out, out)
    exit(array_ops.reshape(out, ()))

if context.executing_eagerly():
    f = def_function.function(overflow_in_float16)
    self.assertEqual(f().numpy(), float('Inf'))
    # Outside a def_function.function, the grappler pass will not be applied.
    self.assertAlmostEqual(overflow_in_float16().numpy(), 2 ** 20)

    # Test disabling mixed precision.
    mixed_precision.disable_mixed_precision_graph_rewrite_v1()
    self.assertEqual(f().numpy(), 2 ** 20)
else:
    with session.Session() as sess:
        out = overflow_in_float16()
        sess.run(var.initializer)
        self.assertEqual(sess.run(out), float('Inf'))

    # Test Session will enable the auto_mixed_precision grappler pass in a
    # ConfigProto passed by the user
    with session.Session(config=config_pb2.ConfigProto()) as sess:
        out = overflow_in_float16()
        sess.run(var.initializer)
        self.assertEqual(sess.run(out), float('Inf'))

    # Test disabling mixed precision.
    mixed_precision.disable_mixed_precision_graph_rewrite_v1()
    with session.Session() as sess:
        out = overflow_in_float16()
        sess.run(var.initializer)
        self.assertAlmostEqual(sess.run(out), 2 ** 20)
