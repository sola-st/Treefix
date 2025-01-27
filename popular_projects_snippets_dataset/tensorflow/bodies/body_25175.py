# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
# Use shorthand alias for the command prefix.
out = self._registry.dispatch_command("lt", ["-s", "op_type", "-r"])
assert_listed_tensors(
    self,
    out, [
        "simple_mul_add/u:0", "simple_mul_add/v:0",
        "simple_mul_add/u/read:0", "simple_mul_add/v/read:0",
        "simple_mul_add/matmul:0", "simple_mul_add/add:0"
    ], [
        "VariableV2", "VariableV2", "Identity", "Identity",
        _matmul_op_name(), "AddV2"
    ],
    sort_by="op_type",
    reverse=True)
check_main_menu(self, out, list_tensors_enabled=False)
