# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graph_reconstruction_test.py
with session.Session(config=self._no_rewrite_session_config()) as sess:
    u = variables.Variable(12.0, name="u")
    v = variables.Variable(30.0, name="v")
    x = constant_op.constant(1.1, name="x")
    toy_loss = x * (u - v)
    train_op = gradient_descent.GradientDescentOptimizer(
        learning_rate=0.1).minimize(toy_loss, name="train_op")
    self.evaluate(u.initializer)
    self.evaluate(v.initializer)

    self._compareOriginalAndReconstructedGraphDefs(sess, train_op)
