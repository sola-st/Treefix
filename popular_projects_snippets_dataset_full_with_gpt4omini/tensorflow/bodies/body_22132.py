# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer_test.py
# Running only in graph mode is useful, because optimizers sometimes return
# a value that, in Graph mode, is runnable with self.evaluate. But in Eager
# mode, the optimizer already does the computations and the return value
# cannot be run.
if not context.executing_eagerly():
    self.evaluate(val)
