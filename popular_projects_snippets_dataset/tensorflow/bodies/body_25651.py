# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
self._orig_screen_output = debugger_cli_common.RichTextLines(
    ["Folk song:", "Roses are red", "Violets are blue"],
    font_attr_segs={1: [(0, 5, "red"), (6, 9, "gray"), (10, 12, "red"),
                        (12, 13, "crimson")],
                    2: [(0, 7, "blue"), (8, 11, "gray"), (12, 14, "blue"),
                        (14, 16, "indigo")]},
    annotations={1: "longer wavelength",
                 2: "shorter wavelength"})
