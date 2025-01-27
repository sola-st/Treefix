# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/arithmetic_optimizer_test.py
exit(math_ops.matmul(
    x, array_ops.reshape(array_ops.transpose(y), [384, 1536])))
