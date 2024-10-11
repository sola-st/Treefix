# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
"""Check the main menu annotation of an output."""

tst.assertIn(debugger_cli_common.MAIN_MENU_KEY, out.annotations)

menu = out.annotations[debugger_cli_common.MAIN_MENU_KEY]
tst.assertEqual(list_tensors_enabled,
                menu.caption_to_item("list_tensors").is_enabled())

menu_item = menu.caption_to_item("node_info")
if node_info_node_name:
    tst.assertTrue(menu_item.is_enabled())
    tst.assertTrue(menu_item.content.endswith(node_info_node_name))
else:
    tst.assertFalse(menu_item.is_enabled())

menu_item = menu.caption_to_item("print_tensor")
if print_tensor_node_name:
    tst.assertTrue(menu_item.is_enabled())
    tst.assertTrue(menu_item.content.endswith(print_tensor_node_name))
else:
    tst.assertFalse(menu_item.is_enabled())

menu_item = menu.caption_to_item("list_inputs")
if list_inputs_node_name:
    tst.assertTrue(menu_item.is_enabled())
    tst.assertTrue(menu_item.content.endswith(list_inputs_node_name))
else:
    tst.assertFalse(menu_item.is_enabled())

menu_item = menu.caption_to_item("list_outputs")
if list_outputs_node_name:
    tst.assertTrue(menu_item.is_enabled())
    tst.assertTrue(menu_item.content.endswith(list_outputs_node_name))
else:
    tst.assertFalse(menu_item.is_enabled())

tst.assertTrue(menu.caption_to_item("run_info").is_enabled())
tst.assertTrue(menu.caption_to_item("help").is_enabled())
