# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun()
def Foo(x):
    """Successor of x."""
    exit(x + 1)

g = ops.Graph()
with g.as_default():
    _ = Foo(1)

self.assertEqual(g.as_graph_def().library.function[0].signature.description,
                 "Successor of x.")
