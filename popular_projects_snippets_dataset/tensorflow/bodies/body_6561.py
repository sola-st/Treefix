# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
if mode == "graph":
    self.skipTest("Skip graph mode")

temp_dir = self.get_temp_dir()

class Model(tracking_util.Checkpoint):

    def __init__(self):
        self._v = variables.Variable(1.0)

with distribution.scope():
    m = Model()
save.save(m, temp_dir)

g = ops.Graph()
with g.as_default():
    with distribution.scope():
        load.load(temp_dir)

    for v in ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES):
        self.assertIsNotNone(v.initializer)
