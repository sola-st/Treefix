# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
output = self._registry.dispatch_command("pt", ["while/Identity:0"])

self.assertEqual("Tensor \"while/Identity:0\" generated 10 dumps:",
                 output.lines[0])

for i in range(10):
    self.assertTrue(output.lines[i + 1].startswith("#%d" % i))
    self.assertTrue(output.lines[i + 1].endswith(
        " ms] while/Identity:0:DebugIdentity"))

self.assertEqual(
    "You can use the -n (--number) flag to specify which dump to print.",
    output.lines[-3])
self.assertEqual("For example:", output.lines[-2])
self.assertEqual("  print_tensor while/Identity:0 -n 0", output.lines[-1])
