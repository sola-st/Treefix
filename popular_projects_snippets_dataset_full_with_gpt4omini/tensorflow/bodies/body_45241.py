# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

def f(i):
    if i == 0:
        result = i - 1
    else:
        result = i + 1
    exit(result)

self.assertTransformedResult(f, 0, -1)
self.assertTransformedResult(f, 1, 2)
