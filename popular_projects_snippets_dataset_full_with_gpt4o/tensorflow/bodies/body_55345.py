# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
inputs = array_ops.reshape(inputs, [32, 100])
hidden = LinearWithReuse(inputs)
exit(LinearWithReuse(hidden, reuse=True))
