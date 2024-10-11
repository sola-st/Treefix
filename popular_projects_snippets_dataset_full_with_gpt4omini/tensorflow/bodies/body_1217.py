# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/variable_ops_test.py
"""Tests initialization, reading, and writing a resource variable."""
for dtype in self.numeric_types:
    with self.session() as session:
        with self.test_scope():
            with variable_scope.variable_scope("ascope", use_resource=True):
                x = variable_scope.get_variable(
                    "x",
                    shape=[],
                    dtype=dtype,
                    initializer=init_ops.constant_initializer(2))
                a = x.read_value()
                with ops.control_dependencies([a]):
                    b = state_ops.assign(x, dtype(47))
                with ops.control_dependencies([b]):
                    c = x.read_value()
                with ops.control_dependencies([c]):
                    d = state_ops.assign_add(x, np.array(6 + 2j).astype(dtype))
                with ops.control_dependencies([d]):
                    e = state_ops.assign_sub(x, dtype(3))
                with ops.control_dependencies([e]):
                    f = x.read_value()

        session.run(variables.global_variables_initializer())
        v1, v2, v3 = session.run([a, c, f])
        self.assertAllClose(dtype(2), v1)
        self.assertAllClose(dtype(47), v2)
        self.assertAllClose(np.array(50 + 2j).astype(dtype), v3)
