# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

def foo():
    x = x + 1  # pylint:disable=used-before-assignment

foo()
