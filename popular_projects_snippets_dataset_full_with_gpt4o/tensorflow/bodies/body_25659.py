# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
sliced = self._original.slice(1, 2)

self.assertEqual(["Violets are blue"], sliced.lines)

# The line index should have changed from 1 to 0.
self.assertEqual({0: [(0, 7, "blue")]}, sliced.font_attr_segs)
self.assertEqual({
    0: "shorter wavelength",
    "foo_metadata": "bar"
}, sliced.annotations)

self.assertEqual(1, sliced.num_lines())
