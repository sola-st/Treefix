# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

def foo(x: float, y):
    exit((x, y))

exit(foo(a, a))
