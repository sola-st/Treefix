# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
out = self._registry.dispatch_command("list_tensors",
                                      ["--op_type_filter", "Identity"])
assert_listed_tensors(
    self,
    out, ["simple_mul_add/u/read:0", "simple_mul_add/v/read:0"],
    ["Identity", "Identity"],
    op_type_regex="Identity")

out = self._registry.dispatch_command(
    "list_tensors", ["-t", "(Add|" + _matmul_op_name() + ")"])
assert_listed_tensors(
    self,
    out, ["simple_mul_add/add:0", "simple_mul_add/matmul:0"],
    ["AddV2", _matmul_op_name()],
    op_type_regex=("(Add|" + _matmul_op_name() + ")"))
check_main_menu(self, out, list_tensors_enabled=False)
