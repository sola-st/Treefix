# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
out = self._registry.dispatch_command(
    "print_tensor", ["simple_mul_add/matmul/foo:0"])

self.assertEqual([
    "ERROR: Node \"simple_mul_add/matmul/foo\" does not exist in partition "
    "graphs"
], out.lines)
check_main_menu(self, out, list_tensors_enabled=True)
