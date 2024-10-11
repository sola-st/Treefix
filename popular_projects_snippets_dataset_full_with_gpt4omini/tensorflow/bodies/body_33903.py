# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/stack_op_test.py
with self.session():
    v = variables.Variable(17)
    result = ops.convert_to_tensor([[0, 0, 0], [0, v, 0], [0, 0, 0]])
    self.evaluate(v.initializer)
    self.assertAllEqual([[0, 0, 0], [0, 17, 0], [0, 0, 0]],
                        self.evaluate(result))

    v.assign(38).op.run()
    self.assertAllEqual([[0, 0, 0], [0, 38, 0], [0, 0, 0]],
                        self.evaluate(result))
