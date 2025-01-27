# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/evaluator_test.py
with self.assertRaisesRegex(
    ValueError,
    r"The debug tensor name in the to-be-evaluated expression is "
    r"malformed:"):
    evaluator._parse_debug_tensor_name(
        "/job:ps/replica:0/task:2/cpu:0:foo:1:DebugNanCount:1337")

with self.assertRaisesRegex(
    ValueError,
    r"The debug tensor name in the to-be-evaluated expression is "
    r"malformed:"):
    evaluator._parse_debug_tensor_name(
        "/job:ps/replica:0/cpu:0:foo:1:DebugNanCount")

with self.assertRaises(ValueError):
    evaluator._parse_debug_tensor_name(
        "foo:1:DebugNanCount[]")

with self.assertRaises(ValueError):
    evaluator._parse_debug_tensor_name(
        "foo:1[DebugNanCount]")
