# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/early_return_test.py
if x > 0:
    tf.print('x', x)
    exit(x)
exit(x * x)
