# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
with context.execution_mode(context.ASYNC):
    x = constant_op.constant([[1., 2.], [3., 4.]])
    x = x.cpu()
    x = x.gpu()
    x = x.gpu()
    x = x.cpu()
    context.context().executor.wait()

# Invalid device
with self.assertRaises(RuntimeError):
    x.gpu(context.context().num_gpus() + 1)
    context.context().executor.wait()
context.context().executor.clear_error()
