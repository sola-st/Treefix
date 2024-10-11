import numpy as np # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.assertEqual = lambda x, y: x == y # pragma: no cover
self._checkTensorMetadata = lambda a, b: None # pragma: no cover
self._findFirst = lambda lines, value: (lines.index(value), 0) # pragma: no cover
out = Mock() # pragma: no cover
out.lines = [ # pragma: no cover
    'Tensor "a":', # pragma: no cover
    '', # pragma: no cover
    '[[1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],', # pragma: no cover
    ' [1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021],', # pragma: no cover
    ' [1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032],', # pragma: no cover
    ' [1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043],', # pragma: no cover
    ' [1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054],', # pragma: no cover
    ' [1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065],', # pragma: no cover
    ' [1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076],', # pragma: no cover
    ' [1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087],', # pragma: no cover
    ' [1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098],', # pragma: no cover
    ' [1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109],', # pragma: no cover
    ' [1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120]]', # pragma: no cover
    '...' # pragma: no cover
] # pragma: no cover

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
