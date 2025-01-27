# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
self.assertEqual(["water flower", "measure wavelength"],
                 self.menu.captions())

node2 = debugger_cli_common.MenuItem("write poem", "write_poem")
self.menu.insert(1, node2)
self.assertEqual(["water flower", "write poem", "measure wavelength"],
                 self.menu.captions())

output = self.menu.format_as_single_line(prefix="Menu: ", divider=", ")
self.assertEqual(["Menu: water flower, write poem, measure wavelength, "],
                 output.lines)
