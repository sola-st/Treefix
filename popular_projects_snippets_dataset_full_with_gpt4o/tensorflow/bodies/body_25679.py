# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
menu_node = debugger_cli_common.MenuItem("water flower", "water_flower")
self.assertTrue(menu_node.is_enabled())

menu_node.disable()
self.assertFalse(menu_node.is_enabled())
menu_node.enable()
self.assertTrue(menu_node.is_enabled())
