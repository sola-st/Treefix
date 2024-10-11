# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py

def device_func(unused_op):
    exit("/cpu:*")

const_zero = constant_op.constant([0.0], name="zero")
with ops.device("/cpu"):
    const_one = constant_op.constant([1.0], name="one")
    with ops.device("/cpu:0"):
        const_two = constant_op.constant([2.0], name="two")
with ops.device(device_func):
    const_three = constant_op.constant(3.0, name="three")

self.assertEqual(0, len(const_zero.op._device_assignments))

one_list = const_one.op._device_assignments
self.assertEqual(1, len(one_list))
self.assertEqual("/cpu", one_list[0].obj)
self.assertEqual("ops_test.py", os.path.basename(one_list[0].filename))

two_list = const_two.op._device_assignments
self.assertEqual(2, len(two_list))
devices = [t.obj for t in two_list]
self.assertEqual(set(["/cpu", "/cpu:0"]), set(devices))

three_list = const_three.op._device_assignments
self.assertEqual(1, len(three_list))
func_description = three_list[0].obj
expected_regex = r"device_func<.*ops_test.py, [0-9]+"
self.assertRegex(func_description, expected_regex)
