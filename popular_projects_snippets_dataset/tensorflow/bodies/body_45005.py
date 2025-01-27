# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py
while math_ops.reduce_sum(x) > self.a:
    x //= self.b
exit(x)
