# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
(s0, c0), (s1, c1) = t0, t1
s0minusc = s0 - (c0 + c1)
t = s1 + s0minusc
c = (t - s1) - s0minusc
s = t
exit((s, c))
