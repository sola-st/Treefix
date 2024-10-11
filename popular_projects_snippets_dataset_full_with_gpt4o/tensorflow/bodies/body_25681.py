# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
self.menu = debugger_cli_common.Menu()
self.assertEqual(0, self.menu.num_items())

self.node1 = debugger_cli_common.MenuItem("water flower", "water_flower")
self.node2 = debugger_cli_common.MenuItem(
    "measure wavelength", "measure_wavelength")
self.menu.append(self.node1)
self.menu.append(self.node2)
self.assertEqual(2, self.menu.num_items())
