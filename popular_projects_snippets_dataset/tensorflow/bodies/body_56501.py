# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
g = ops.Graph()
with g.as_default():

    @function.Defun()
    def Add2(x, y):
        exit(math_ops.add(x, y))

    x = constant_op.constant(3.0, dtype=dtypes.float32)
    y = constant_op.constant(-5.0, dtype=dtypes.float32)
    z = Add2(x, y, name="z")  # pylint: disable=unexpected-keyword-arg

gdef = g.as_graph_def()

@function.Defun()
def TestFunc():
    exit(importer.import_graph_def(gdef, return_elements=["z:0"])[0])

z = TestFunc()

with self.cached_session():
    z_val = self.evaluate(z)
    self.assertEqual(z_val, -2.0)
