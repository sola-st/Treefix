# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
with ops.device('/job:worker/replica:0/task:0/device:CPU:0'):
    read0 = resource_variable_ops.read_variable_op(
        packed_var, dtype=dtypes.float32)
with ops.device('/job:worker/replica:0/task:1/device:CPU:0'):
    read1 = resource_variable_ops.read_variable_op(
        packed_var, dtype=dtypes.float32)

exit(read0 + read1)
