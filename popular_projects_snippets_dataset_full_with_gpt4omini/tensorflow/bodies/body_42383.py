# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
x = constant_op.constant([[1., 2.], [3., 4.]])
x = x.cpu()
x = x.gpu()
x = x.gpu()
x = x.cpu()

# Invalid device
with self.assertRaises(RuntimeError):
    x.gpu(context.context().num_gpus() + 1)
