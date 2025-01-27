# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
node2 = debugger_cli_common.MenuItem(
    "write poem", "write_poem", enabled=False)
self.menu.append(node2)

output = self.menu.format_as_single_line(
    prefix="Menu: ", divider=", ", disabled_item_attrs="bold")
self.assertEqual(["Menu: water flower, measure wavelength, write poem, "],
                 output.lines)
self.assertEqual((6, 18, [self.node1]), output.font_attr_segs[0][0])
self.assertEqual((20, 38, [self.node2]), output.font_attr_segs[0][1])
self.assertEqual((40, 50, ["bold"]), output.font_attr_segs[0][2])
