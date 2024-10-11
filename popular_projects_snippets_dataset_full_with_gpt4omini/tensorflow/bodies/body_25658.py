# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
sliced = self._original.slice(0, 1)

self.assertEqual(["Roses are red"], sliced.lines)
self.assertEqual({0: [(0, 5, "red")]}, sliced.font_attr_segs)

# Non-line-number metadata should be preserved.
self.assertEqual({
    0: "longer wavelength",
    "foo_metadata": "bar"
}, sliced.annotations)

self.assertEqual(1, sliced.num_lines())
