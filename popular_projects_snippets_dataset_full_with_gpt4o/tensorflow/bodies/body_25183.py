# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
"""Test register and invoke a tensor filter."""

# First, register the filter.
self._analyzer.add_tensor_filter("has_inf_or_nan",
                                 debug_data.has_inf_or_nan)

# Use shorthand alias for the command prefix.
out = self._registry.dispatch_command("lt", ["-f", "has_inf_or_nan"])

# This TF graph run did not generate any bad numerical values.
assert_listed_tensors(
    self, out, [], [], tensor_filter_name="has_inf_or_nan")
# TODO(cais): A test with some actual bad numerical values.

check_main_menu(self, out, list_tensors_enabled=False)
