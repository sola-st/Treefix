# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/evaluator_test.py
device_name, node_name, output_slot, debug_op, exec_index = (
    evaluator._parse_debug_tensor_name("foo:1[20]"))
self.assertIsNone(device_name)
self.assertEqual("foo", node_name)
self.assertEqual(1, output_slot)
self.assertEqual("DebugIdentity", debug_op)
self.assertEqual(20, exec_index)

device_name, node_name, output_slot, debug_op, exec_index = (
    evaluator._parse_debug_tensor_name("hidden_0/Weights:0[3]"))
self.assertIsNone(device_name)
self.assertEqual("hidden_0/Weights", node_name)
self.assertEqual(0, output_slot)
self.assertEqual("DebugIdentity", debug_op)
self.assertEqual(3, exec_index)
