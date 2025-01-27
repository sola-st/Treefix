# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
self._original = debugger_cli_common.RichTextLines(
    ["Roses are red", "Violets are blue"],
    font_attr_segs={0: [(0, 5, "red")],
                    1: [(0, 7, "blue")]},
    annotations={
        0: "longer wavelength",
        1: "shorter wavelength",
        "foo_metadata": "bar"
    })
