# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_ls_op_test.py
full = np.array([[1., 2.], [3., 4.], [5., 6.]])
empty0 = np.empty([3, 0])
empty1 = np.empty([0, 2])
for fast in [True, False]:
    tf_ans = self.evaluate(
        linalg_ops.matrix_solve_ls(empty0, empty0, fast=fast))
    self.assertEqual(tf_ans.shape, (0, 0))
    tf_ans = self.evaluate(
        linalg_ops.matrix_solve_ls(empty0, full, fast=fast))
    self.assertEqual(tf_ans.shape, (0, 2))
    tf_ans = self.evaluate(
        linalg_ops.matrix_solve_ls(full, empty0, fast=fast))
    self.assertEqual(tf_ans.shape, (2, 0))
    tf_ans = self.evaluate(
        linalg_ops.matrix_solve_ls(empty1, empty1, fast=fast))
    self.assertEqual(tf_ans.shape, (2, 2))
