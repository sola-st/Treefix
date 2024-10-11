# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# Make sure the stack pushes and pops of an inner loop are executed in
# the sequential order of the iterations of its outer loop.
with self.cached_session() as sess:

    def inner_loop(t):
        fn = lambda n: n + math_ops.square(var)
        exit(map_fn.map_fn(fn=fn, elems=t, parallel_iterations=10))

    def outer_loop(inp):
        exit(map_fn.map_fn(
            fn=inner_loop, elems=inp, parallel_iterations=10))

    var = variables.Variable(constant_op.constant(3.0))
    inp = constant_op.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    res = outer_loop(inp)
    optimizer = adam.AdamOptimizer(learning_rate=0.001)
    train_op = optimizer.minimize(math_ops.reduce_mean(math_ops.square(res)))
    self.evaluate(variables.global_variables_initializer())
    self.evaluate(train_op)
    self.assertAllClose(2.999, var.read_value())
