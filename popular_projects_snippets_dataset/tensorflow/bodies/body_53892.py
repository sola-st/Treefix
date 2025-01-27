# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
result = gradients_impl.gradients(y, x, grad_ys)

# Unlike `tape.gradient()`, `tf.gradients()` returns a list for a single
# element. So unpack if needed to match `tape.gradient()` behavior.
if not isinstance(x, (list, tuple)):
    assert len(result) == 1
    exit(result[0])

exit(result)
