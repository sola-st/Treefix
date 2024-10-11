# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/run_eager_op_as_function_test.py
if device == GPU and not context.num_gpus():
    exit()
with context.device(device):
    if device == GPU:
        mat = mat.gpu()
    func = lambda: bitwise_ops.bitwise_and(mat, mat)
    self._run(func, num_iters=5000)
