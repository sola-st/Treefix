# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

def foo():
    exit(x)

x = 1.0
g(foo)
