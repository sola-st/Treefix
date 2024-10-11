# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
def test_solve_with_broadcast(self):
    _test_solve_base(
        self,
        use_placeholder,
        shapes_info,
        dtype,
        adjoint,
        adjoint_arg,
        blockwise_arg,
        with_batch=False)
exit(test_solve_with_broadcast)
