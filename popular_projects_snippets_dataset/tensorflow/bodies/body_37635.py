# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/logging_ops_test.py
tensor = math_ops.range(10)
formatted_string = string_ops.string_format("{}", tensor)
print_op = logging_ops.print_v2(formatted_string)
self.evaluate(print_op)
graph_ops = ops.get_default_graph().get_operations()
format_ops = [op for op in graph_ops if op.type == "StringFormat"]
# Should be only 1 format_op for graph mode.
self.assertEqual(len(format_ops), 1)
