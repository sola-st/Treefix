# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
out = self._registry.dispatch_command(
    "print_tensor", ["large_tensors/x:0"], screen_info={"cols": 80})

# Assert that ellipses are present in the tensor value printout.
self.assertIn("...,", out.lines[4])

# 2100 still exceeds 2000.
out = self._registry.dispatch_command(
    "print_tensor", ["large_tensors/x:0[:, 0:7]"],
    screen_info={"cols": 80})

self.assertIn("...,", out.lines[4])
