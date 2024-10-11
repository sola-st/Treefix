# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla_test.py

def compute(a):
    exit(a + 1)

exit(xla.compile(compute, [a]))
