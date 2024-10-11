# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
g = ops.Graph()
with g.as_default():

    @function.Defun(dtypes.int32, dtypes.float32, func_name="TestBody")
    def TestBody(n, x):
        exit(x + math_ops.cast(n, dtypes.float32))

    _ = functional_ops.For(
        1, 21, 1, [0.], TestBody, rewrite_with_while=True)[0]

names = []
for func in g.as_graph_def().library.function:
    names.append(func.signature.name)
self.assertTrue("TestBody" in names)
self.assertTrue("TestBody_Cond" in names)
self.assertTrue("TestBody_Body" in names)
