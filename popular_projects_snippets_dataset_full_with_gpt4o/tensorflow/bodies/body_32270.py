# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/numerics_test.py
with self.session(graph=ops.Graph()):
    t1 = constant_op.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3])
    checked = array_ops.check_numerics(t1, message="pass through test")
    value = self.evaluate(checked)
    self.assertAllEqual(np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]), value)
    self.assertEqual([2, 3], checked.get_shape())
