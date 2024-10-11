# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
const_two = constant_op.constant([2.0], name="two")
with ops.colocate_with(const_two.op):
    const_three = constant_op.constant(3.0, name="three")
locations_dict = const_three.op._colocation_dict
self.assertIn("two", locations_dict)
metadata = locations_dict["two"]
self.assertIsNone(metadata.obj)
# Check that this test's filename is recorded as the file containing the
# colocation statement.
self.assertEqual("ops_test.py", os.path.basename(metadata.filename))
