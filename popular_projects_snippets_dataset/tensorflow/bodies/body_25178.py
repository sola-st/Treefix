# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
out = self._registry.dispatch_command("list_tensors",
                                      ["--node_name_filter", ".*read.*"])
assert_listed_tensors(
    self,
    out, ["simple_mul_add/u/read:0", "simple_mul_add/v/read:0"],
    ["Identity", "Identity"],
    node_name_regex=".*read.*")

out = self._registry.dispatch_command("list_tensors", ["-n", "^read"])
assert_listed_tensors(self, out, [], [], node_name_regex="^read")
check_main_menu(self, out, list_tensors_enabled=False)
