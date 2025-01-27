# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
output = self.menu.format_as_single_line(
    prefix="Menu: ", divider=", ", enabled_item_attrs="underline")
self.assertEqual(["Menu: water flower, measure wavelength, "], output.lines)
self.assertEqual((6, 18, [self.node1, "underline"]),
                 output.font_attr_segs[0][0])
self.assertEqual((20, 38, [self.node2, "underline"]),
                 output.font_attr_segs[0][1])
self.assertEqual({}, output.annotations)
