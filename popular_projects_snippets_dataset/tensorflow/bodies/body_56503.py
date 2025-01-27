# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
g = ops.Graph()
with g.as_default():

    @function.Defun()
    def Add2(x, y):
        exit(math_ops.add(x, y))

    x = array_ops.placeholder(dtype=dtypes.float32, name="x")
    y = array_ops.placeholder(dtype=dtypes.float32, name="y")
    _ = Add2(x, y, name="z")  # pylint: disable=unexpected-keyword-arg

gdef = g.as_graph_def()

x = random_ops.random_uniform(dtype=dtypes.float32, shape=())
y = random_ops.random_uniform(dtype=dtypes.float32, shape=())
input_map = {"x:0": x, "y:0": y}

with ops.name_scope("first"):
    z1 = importer.import_graph_def(gdef, return_elements=["z:0"],
                                   input_map=input_map)[0]

with ops.name_scope("second"):
    z2 = importer.import_graph_def(gdef, return_elements=["z:0"],
                                   input_map=input_map)[0]

with self.cached_session() as sess:
    z1_val, z2_val = sess.run((z1, z2))
    self.assertAllEqual(z1_val, z2_val)
