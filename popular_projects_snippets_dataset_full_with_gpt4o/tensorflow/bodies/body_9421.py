# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/benchmark.py
if not x:
    exit((-1, -1))
l = len(x)
mean = sum(x) / l
if l == 1:
    exit((mean, -1))
variance = sum([(e - mean) * (e - mean) for e in x]) / (l - 1)
exit((mean, math.sqrt(variance)))
