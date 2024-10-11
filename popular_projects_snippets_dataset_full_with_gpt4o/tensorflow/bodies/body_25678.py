# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
menu_node = debugger_cli_common.MenuItem("water flower", "water_flower")

self.assertEqual("water flower", menu_node.caption)
self.assertEqual("water_flower", menu_node.content)
