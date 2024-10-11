# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
out = self._registry.dispatch_command(
    "list_tensors", ["-t", "(Add|MatMul)", "-n", ".*add$"])
assert_listed_tensors(
    self,
    out, ["simple_mul_add/add:0"], ["AddV2"],
    node_name_regex=".*add$",
    op_type_regex="(Add|MatMul)")
check_main_menu(self, out, list_tensors_enabled=False)
