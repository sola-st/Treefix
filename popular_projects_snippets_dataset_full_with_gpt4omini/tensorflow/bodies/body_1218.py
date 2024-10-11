# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/variable_ops_test.py
"""Tests a gradient descent step for a simple model."""
with self.session() as session:
    with self.test_scope():
        with variable_scope.variable_scope("ascope", use_resource=True):
            w = variable_scope.get_variable(
                "w",
                shape=[4, 2],
                dtype=dtypes.float32,
                initializer=init_ops.constant_initializer(
                    np.array([[1, 2], [3, 4], [5, 6], [7, 8]], dtype=np.float32)))
            b = variable_scope.get_variable(
                "b",
                shape=[2],
                dtype=dtypes.float32,
                initializer=init_ops.constant_initializer(
                    np.array([2, 3], dtype=np.float32)))

            x = array_ops.placeholder(dtypes.float32, shape=[1, 4])
            y = math_ops.matmul(x, w) + b
            loss = math_ops.reduce_sum(y)
            optimizer = GradientDescentOptimizer(0.1)
            train = optimizer.minimize(loss)

    session.run(variables.global_variables_initializer())
    session.run(train, {x: np.array([[7, 3, 5, 9]], dtype=np.float32)})
    vw, vb = session.run([w, b])
    self.assertAllClose(
        np.array(
            [[0.3, 1.3], [2.7, 3.7], [4.5, 5.5], [6.1, 7.1]],
            dtype=np.float32),
        vw,
        rtol=1e-4)
    self.assertAllClose(np.array([1.9, 2.9], dtype=np.float32), vb, rtol=1e-4)
