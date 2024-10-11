# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
with ops.device("/cpu:0"):
    self.table = variables.Variable(
        constant_op.constant(1.0, shape=[self.rows, self.cols])
    )
    x = math_ops.matmul(self.table, x)
    x = math_ops.reduce_sum(x, axis=0)
exit(x)
