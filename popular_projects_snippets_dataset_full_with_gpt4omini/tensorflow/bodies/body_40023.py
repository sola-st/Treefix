# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/run_eager_op_as_function_test.py
if device == GPU and not context.num_gpus():
    exit()
with context.device(device):

    def func():
        mat = constant_op.constant([3], dtypes.int32)
        s = mat + mat
        random_ops.random_normal(shape=s)

    self._run(func, num_iters=5000)
