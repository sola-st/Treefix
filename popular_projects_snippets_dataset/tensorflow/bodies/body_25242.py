# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
for i in range(5):
    output = self._registry.dispatch_command(
        "pt", ["while/Identity:0", "-n", "%d" % i])

    self.assertEqual("Tensor \"while/Identity:0:DebugIdentity (dump #%d)\":" %
                     i, output.lines[0])
    self.assertEqual("  dtype: int32", output.lines[1])
    self.assertEqual("  shape: ()", output.lines[2])
    self.assertEqual("", output.lines[3])
    self.assertTrue(output.lines[4].startswith("array(%d" % i))
    self.assertTrue(output.lines[4].endswith(")"))
