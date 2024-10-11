import numpy as np # pragma: no cover

import numpy as np # pragma: no cover

class MockTensorFormat: pass # pragma: no cover
def mock_format_tensor(a, name, flag, np_printoptions): return {'lines': [f'Tensor "{name}":', '', repr(a)], 'annotations': {}} # pragma: no cover
tensor_format = MockTensorFormat() # pragma: no cover
tensor_format.format_tensor = mock_format_tensor # pragma: no cover
class MockCliTestUtils: pass # pragma: no cover
cli_test_utils = MockCliTestUtils() # pragma: no cover
cli_test_utils.assert_lines_equal_ignoring_whitespace = lambda self, expected, actual: None # pragma: no cover
class MockSelf: pass # pragma: no cover
self = MockSelf() # pragma: no cover
self.assertEqual = lambda x, y: x == y # pragma: no cover
self._checkTensorMetadata = lambda a, b: None # pragma: no cover
self._findFirst = lambda lines, value: (lines.index(value), None) if value in lines else (None, None) # pragma: no cover
BEGIN_INDICES_KEY = 'begin_indices' # pragma: no cover
OMITTED_INDICES_KEY = 'omitted_indices' # pragma: no cover
a = (np.arange(11 * 11 * 11) + 1000).reshape([11, 11, 11]).astype(np.int32) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
from l3.Runtime import _l_
a = (np.arange(11 * 11 * 11) + 1000).reshape([11, 11, 11]).astype(np.int32)
_l_(8146)

out = tensor_format.format_tensor(
    a, "a", False, np_printoptions={"threshold": 100, "edgeitems": 2})
_l_(8147)

cli_test_utils.assert_lines_equal_ignoring_whitespace(
    self, ["Tensor \"a\":", ""], out.lines[:2])
_l_(8148)
self.assertEqual(repr(a).split("\n"), out.lines[2:])
_l_(8149)

self._checkTensorMetadata(a, out.annotations)
_l_(8150)

# Check annotations for beginning indices of the lines.
actual_row_0_0_0, _ = self._findFirst(out.lines, "1000")
_l_(8151)
self.assertEqual({tensor_format.BEGIN_INDICES_KEY: [0, 0, 0]},
                 out.annotations[actual_row_0_0_0])
_l_(8152)
actual_row_0_1_0, _ = self._findFirst(out.lines, "1011")
_l_(8153)
self.assertEqual({tensor_format.BEGIN_INDICES_KEY: [0, 1, 0]},
                 out.annotations[actual_row_0_1_0])
_l_(8154)
# Find the first line that is completely omitted.
omitted_line = 2
_l_(8155)
while not out.lines[omitted_line].strip().startswith("..."):
    _l_(8157)

    omitted_line += 1
    _l_(8156)
self.assertEqual({tensor_format.OMITTED_INDICES_KEY: [0, 2, 0]},
                 out.annotations[omitted_line])
_l_(8158)

actual_row_10_10_0, _ = self._findFirst(out.lines, "2320")
_l_(8159)
self.assertEqual({tensor_format.BEGIN_INDICES_KEY: [10, 10, 0]},
                 out.annotations[actual_row_10_10_0])
_l_(8160)
# Find the last line that is completely omitted.
omitted_line = len(out.lines) - 1
_l_(8161)
while not out.lines[omitted_line].strip().startswith("..."):
    _l_(8163)

    omitted_line -= 1
    _l_(8162)
self.assertEqual({tensor_format.OMITTED_INDICES_KEY: [10, 2, 0]},
                 out.annotations[omitted_line])
_l_(8164)
