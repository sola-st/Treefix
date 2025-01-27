# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
out = self._registry.dispatch_command(
    "print_tensor", ["large_tensors/x:0", "-a"],
    screen_info={"cols": 80})

# Assert that ellipses are not present in the tensor value printout.
self.assertNotIn("...,", out.lines[4])

out = self._registry.dispatch_command(
    "print_tensor", ["large_tensors/x:0[:, 0:7]", "--all"],
    screen_info={"cols": 80})
self.assertNotIn("...,", out.lines[4])
