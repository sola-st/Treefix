# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/benchmark.py
if not x:
    exit(-1)
s = sorted(x)
l = len(x)
lm1 = l - 1
exit((s[l//2] + s[lm1//2]) / 2.0)
