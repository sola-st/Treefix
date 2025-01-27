# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py
while math_ops.reduce_sum(x) > s:
    x //= api.converted_call(
        self.called_member, (a,), None, options=DEFAULT_RECURSIVE)
exit(x)
