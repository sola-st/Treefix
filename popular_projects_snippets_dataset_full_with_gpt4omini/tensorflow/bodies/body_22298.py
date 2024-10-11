# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer_test.py
with self.cached_session():
    var0 = variables.Variable([1.0, 2.0])
    var1 = variables.Variable([3.0, 4.0])
    cost = 5 * var0 + 3 * var1
    global_step = variables.Variable(
        array_ops.zeros([], dtypes.int64), name='global_step')
    sgd_op = gradient_descent.GradientDescentOptimizer(3.0)
    opt_op = sgd_op.minimize(cost, global_step, [var0, var1])
    self.assertTrue(opt_op in ops.get_collection(ops.GraphKeys.TRAIN_OP))
