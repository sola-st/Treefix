# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
from l3.Runtime import _l_
a = (np.arange(11 * 11 * 11) + 1000).reshape([11, 11, 11]).astype(np.int32)
_l_(20799)

out = tensor_format.format_tensor(
    a, "a", False, np_printoptions={"threshold": 100, "edgeitems": 2})
_l_(20800)

cli_test_utils.assert_lines_equal_ignoring_whitespace(
    self, ["Tensor \"a\":", ""], out.lines[:2])
_l_(20801)
self.assertEqual(repr(a).split("\n"), out.lines[2:])
_l_(20802)

self._checkTensorMetadata(a, out.annotations)
_l_(20803)

# Check annotations for beginning indices of the lines.
actual_row_0_0_0, _ = self._findFirst(out.lines, "1000")
_l_(20804)
self.assertEqual({tensor_format.BEGIN_INDICES_KEY: [0, 0, 0]},
                 out.annotations[actual_row_0_0_0])
_l_(20805)
actual_row_0_1_0, _ = self._findFirst(out.lines, "1011")
_l_(20806)
self.assertEqual({tensor_format.BEGIN_INDICES_KEY: [0, 1, 0]},
                 out.annotations[actual_row_0_1_0])
_l_(20807)
# Find the first line that is completely omitted.
omitted_line = 2
_l_(20808)
while not out.lines[omitted_line].strip().startswith("..."):
    _l_(20810)

    omitted_line += 1
    _l_(20809)
self.assertEqual({tensor_format.OMITTED_INDICES_KEY: [0, 2, 0]},
                 out.annotations[omitted_line])
_l_(20811)

actual_row_10_10_0, _ = self._findFirst(out.lines, "2320")
_l_(20812)
self.assertEqual({tensor_format.BEGIN_INDICES_KEY: [10, 10, 0]},
                 out.annotations[actual_row_10_10_0])
_l_(20813)
# Find the last line that is completely omitted.
omitted_line = len(out.lines) - 1
_l_(20814)
while not out.lines[omitted_line].strip().startswith("..."):
    _l_(20816)

    omitted_line -= 1
    _l_(20815)
self.assertEqual({tensor_format.OMITTED_INDICES_KEY: [10, 2, 0]},
                 out.annotations[omitted_line])
_l_(20817)
