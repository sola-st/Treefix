# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/evaluator_test.py
device_name, node_name, output_slot, debug_op, exec_index = (
    evaluator._parse_debug_tensor_name(
        "/job:ps/replica:0/task:2/cpu:0:foo:1:DebugNanCount"))
self.assertEqual("/job:ps/replica:0/task:2/cpu:0", device_name)
self.assertEqual("foo", node_name)
self.assertEqual(1, output_slot)
self.assertEqual("DebugNanCount", debug_op)
self.assertEqual(0, exec_index)

device_name, node_name, output_slot, debug_op, exec_index = (
    evaluator._parse_debug_tensor_name(
        "/job:worker/replica:0/task:3/gpu:0:"
        "hidden_0/Weights:0:DebugNumericSummary"))
self.assertEqual("/job:worker/replica:0/task:3/gpu:0", device_name)
self.assertEqual("hidden_0/Weights", node_name)
self.assertEqual(0, output_slot)
self.assertEqual("DebugNumericSummary", debug_op)
self.assertEqual(0, exec_index)
