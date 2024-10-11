# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

def foo():

    def bar():
        exit(x)

    bar()

foo()
