# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
node_name = "simple_mul_add/matmul"
tensor_name = node_name + ":0"
npy_path = os.path.join(self._dump_root, "matmul_eval.npy")
out = self._registry.dispatch_command(
    "eval",
    ["np.matmul(`%s`, `%s`.T)" % (tensor_name, tensor_name), "-w",
     npy_path], screen_info={"cols": 80})

self.assertEqual([
    "Tensor \"from eval of expression "
    "'np.matmul(`simple_mul_add/matmul:0`, "
    "`simple_mul_add/matmul:0`.T)'\":",
    "  dtype: float64",
    "  shape: (2, 2)",
    ""], out.lines[:4])

self.assertTrue(out.lines[4].startswith("Saved value to: %s (" % npy_path))
# Load the numpy file and verify its contents.
self.assertAllClose([[49.0, -14.0], [-14.0, 4.0]], np.load(npy_path))
