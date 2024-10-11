# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
node_name = "simple_mul_add/matmul"
tensor_name = node_name + ":0"
out = self._registry.dispatch_command(
    "print_tensor", [tensor_name + "[1, foo()]"], screen_info={"cols": 80})

self.assertEqual("Error occurred during handling of command: print_tensor "
                 + tensor_name + "[1, foo()]:", out.lines[0])
self.assertEqual("ValueError: Invalid tensor-slicing string.",
                 out.lines[-2])
