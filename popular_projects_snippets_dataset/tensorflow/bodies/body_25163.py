# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
attr_segs = out.font_attr_segs[line_index]
found_menu_item = False
for begin, end, attribute in attr_segs:
    attributes = [attribute] if not isinstance(attribute, list) else attribute
    menu_item = [attribute for attribute in attributes if
                 isinstance(attribute, debugger_cli_common.MenuItem)]
    if menu_item:
        tst.assertEqual(expected_begin, begin)
        tst.assertEqual(expected_end, end)
        tst.assertEqual(expected_command, menu_item[0].content)
        found_menu_item = True
        break
tst.assertTrue(found_menu_item)
