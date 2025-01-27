# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
out = self._registry.dispatch_command("lt", ["-s", "dump_size"])
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
    sort_by="dump_size")
check_main_menu(self, out, list_tensors_enabled=False)
