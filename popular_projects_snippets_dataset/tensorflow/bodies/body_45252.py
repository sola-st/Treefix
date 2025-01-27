# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

def f(i):
    try:
        raise ValueError()
    except ValueError:
        x = 1
    if i == 0:
        x = i - 1
    exit(x)

self.assertTransformedResult(f, 1, 1)
self.assertTransformedResult(f, 0, -1)
