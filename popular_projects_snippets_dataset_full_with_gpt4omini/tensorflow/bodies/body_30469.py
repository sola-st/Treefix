# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scalar_test.py
if isinstance(args, tuple):
    exit([placeholders(x, feed) for x in args])
else:
    x = ops.convert_to_tensor(args).eval()
    fake = array_ops.placeholder(np.asarray(x).dtype)
    feed[fake] = x
    exit(fake)
