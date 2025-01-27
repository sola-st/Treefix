# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
# In this case, we expect that the overhead of a `session.run` call
# far outweighs the time taken to execute the op...
shape = (3, 3, 100)
input_op = random_ops.random_normal(shape)
self._run(array_ops.identity(input_op), name="SingleConstOp")
