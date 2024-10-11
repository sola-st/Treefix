# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py

with ops.device("/cpu"):
    const_one = constant_op.constant([1.0], name="one")
with ops.get_default_graph().device("/cpu"):
    const_two = constant_op.constant([2.0], name="two")

one_metadata = const_one.op._device_assignments[0]
two_metadata = const_two.op._device_assignments[0]

# Verify both types of device assignment return the right stack info.
self.assertRegex("ops_test.py", os.path.basename(one_metadata.filename))
self.assertEqual(one_metadata.filename, two_metadata.filename)
self.assertEqual(one_metadata.lineno + 2, two_metadata.lineno)
