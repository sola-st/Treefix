# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([2, 2], dtypes.float32)])
def defun_matmul(m):
    exit(math_ops.matmul(m, m))

func = lambda: defun_matmul(m)
self._run(func, num_iters, execution_mode=execution_mode)
