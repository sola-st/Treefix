# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default() as g:
    # No device.
    a = constant_op.constant(3.0, name="a")

    with ops.device("/cpu:0"):
        b = constant_op.constant(4.0, name="b")
    with ops.device("/job:worker"):
        c = constant_op.constant(5.0, name="c")

gdef = g.as_graph_def()

with ops.Graph().as_default():
    a2, b2, c2 = importer.import_graph_def(
        gdef, return_elements=["a", "b", "c"])
    self.assertEqual(a.device, a2.device)
    self.assertEqual(b.device, b2.device)
    self.assertEqual(c.device, c2.device)

with ops.Graph().as_default():
    with ops.device(device.merge_device("/task:0")):
        a3, b3, c3 = importer.import_graph_def(
            gdef, return_elements=["a", "b", "c"])
        self.assertEqual("/task:0", a3.device)
        self.assertEqual("/task:0/device:CPU:0", b3.device)  # canonicalized.
        self.assertEqual(c.device + "/task:0", c3.device)

with ops.Graph().as_default():
    with ops.device(device.merge_device("/job:ps")):
        a4, b4, c4 = importer.import_graph_def(
            gdef, return_elements=["a", "b", "c"])
        self.assertEqual("/job:ps", a4.device)
        self.assertEqual("/job:ps/device:CPU:0", b4.device)  # canonicalized.
        self.assertEqual(c.device, c4.device)  # worker overrides ps.

with ops.Graph().as_default():
    with ops.device(device.merge_device("/device:GPU:0")):
        a5, b5, c5 = importer.import_graph_def(
            gdef, return_elements=["a", "b", "c"])
        self.assertEqual("/device:GPU:0", a5.device)
        self.assertEqual("/device:CPU:0", b5.device)  # cpu overrides gpu.
        self.assertEqual(c.device + "/device:GPU:0", c5.device)
