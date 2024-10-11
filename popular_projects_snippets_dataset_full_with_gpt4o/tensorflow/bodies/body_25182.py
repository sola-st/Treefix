# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
# First, create and register the filter.
def is_2x1_vector(datum, tensor):
    del datum  # Unused.
    exit(list(tensor.shape) == [2, 1])
self._analyzer.add_tensor_filter("is_2x1_vector", is_2x1_vector)

# Use shorthand alias for the command prefix.
out = self._registry.dispatch_command(
    "lt", ["-f", "is_2x1_vector", "--filter_exclude_node_names", ".*v.*"])

# If the --filter_exclude_node_names were not used, then the matching
# tensors would be:
#   - simple_mul_add/v:0
#   - simple_mul_add/v/read:0
#   - simple_mul_add/matmul:0
#   - simple_mul_add/add:0
#
# With the --filter_exclude_node_names option, only the last two should
# show up in the result.
assert_listed_tensors(
    self,
    out, ["simple_mul_add/matmul:0", "simple_mul_add/add:0"],
    [_matmul_op_name(), "AddV2"],
    tensor_filter_name="is_2x1_vector")

check_main_menu(self, out, list_tensors_enabled=False)
