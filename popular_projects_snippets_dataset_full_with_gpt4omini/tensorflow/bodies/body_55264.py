# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32, func_name="Duplicate")
def Duplicate(a):
    b = a + 1.0
    exit((b, b))

g = ops.Graph()
with g.as_default():
    Duplicate([3.0])
    func_sig = g.as_graph_def().library.function[0].signature
    # The names given to both outputs should be different
    # even though the same tensor is emitted to both.
    out_names = [a.name for a in func_sig.output_arg]
    self.assertEqual(2, len(out_names))
    self.assertNotEqual(out_names[0], out_names[1])
