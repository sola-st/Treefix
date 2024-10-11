# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
node_name = "simple_mul_add/matmul"
tensor_name = node_name + ":0"
npy_path = os.path.join(self._dump_root, "matmul.npy")
out = self._registry.dispatch_command(
    "print_tensor", [tensor_name, "-w", npy_path],
    screen_info={"cols": 80})

self.assertEqual([
    "Tensor \"%s:DebugIdentity\":" % tensor_name,
    "  dtype: float64",
    "  shape: (2, 1)",
    "",
], out.lines[:4])
self.assertTrue(out.lines[4].startswith("Saved value to: %s (" % npy_path))
# Load the numpy file and verify its contents.
self.assertAllClose([[7.0], [-2.0]], np.load(npy_path))
