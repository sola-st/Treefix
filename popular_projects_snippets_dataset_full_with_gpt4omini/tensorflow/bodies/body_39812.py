# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
def_function.run_functions_eagerly(run_eager)
with context.device(CPU):
    m = self._m_2_by_2.cpu()
    self._benchmark_defun_matmul_forward_backward(
        m,
        transpose_b=False,
        num_iters=self._num_iters_2_by_2,
        execution_mode=context.ASYNC)
