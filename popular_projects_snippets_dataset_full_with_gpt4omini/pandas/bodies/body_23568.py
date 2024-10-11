# Extracted from ./data/repos/pandas/pandas/io/stata.py

# type          code.
# --------------------
# str1        1 = 0x01
# str2        2 = 0x02
# ...
# str244    244 = 0xf4
# byte      251 = 0xfb  (sic)
# int       252 = 0xfc
# long      253 = 0xfd
# float     254 = 0xfe
# double    255 = 0xff
# --------------------
# NOTE: the byte type seems to be reserved for categorical variables
# with a label, but the underlying variable is -127 to 100
# we're going to drop the label and cast to int
self.DTYPE_MAP = dict(
    list(zip(range(1, 245), [np.dtype("a" + str(i)) for i in range(1, 245)]))
    + [
        (251, np.dtype(np.int8)),
        (252, np.dtype(np.int16)),
        (253, np.dtype(np.int32)),
        (254, np.dtype(np.float32)),
        (255, np.dtype(np.float64)),
    ]
)
self.DTYPE_MAP_XML: dict[int, np.dtype] = {
    32768: np.dtype(np.uint8),  # Keys to GSO
    65526: np.dtype(np.float64),
    65527: np.dtype(np.float32),
    65528: np.dtype(np.int32),
    65529: np.dtype(np.int16),
    65530: np.dtype(np.int8),
}
self.TYPE_MAP = list(tuple(range(251)) + tuple("bhlfd"))
self.TYPE_MAP_XML = {
    # Not really a Q, unclear how to handle byteswap
    32768: "Q",
    65526: "d",
    65527: "f",
    65528: "l",
    65529: "h",
    65530: "b",
}
# NOTE: technically, some of these are wrong. there are more numbers
# that can be represented. it's the 27 ABOVE and BELOW the max listed
# numeric data type in [U] 12.2.2 of the 11.2 manual
float32_min = b"\xff\xff\xff\xfe"
float32_max = b"\xff\xff\xff\x7e"
float64_min = b"\xff\xff\xff\xff\xff\xff\xef\xff"
float64_max = b"\xff\xff\xff\xff\xff\xff\xdf\x7f"
self.VALID_RANGE = {
    "b": (-127, 100),
    "h": (-32767, 32740),
    "l": (-2147483647, 2147483620),
    "f": (
        np.float32(struct.unpack("<f", float32_min)[0]),
        np.float32(struct.unpack("<f", float32_max)[0]),
    ),
    "d": (
        np.float64(struct.unpack("<d", float64_min)[0]),
        np.float64(struct.unpack("<d", float64_max)[0]),
    ),
}

self.OLD_TYPE_MAPPING = {
    98: 251,  # byte
    105: 252,  # int
    108: 253,  # long
    102: 254,  # float
    100: 255,  # double
}

# These missing values are the generic '.' in Stata, and are used
# to replace nans
self.MISSING_VALUES = {
    "b": 101,
    "h": 32741,
    "l": 2147483621,
    "f": np.float32(struct.unpack("<f", b"\x00\x00\x00\x7f")[0]),
    "d": np.float64(
        struct.unpack("<d", b"\x00\x00\x00\x00\x00\x00\xe0\x7f")[0]
    ),
}
self.NUMPY_TYPE_MAP = {
    "b": "i1",
    "h": "i2",
    "l": "i4",
    "f": "f4",
    "d": "f8",
    "Q": "u8",
}

# Reserved words cannot be used as variable names
self.RESERVED_WORDS = (
    "aggregate",
    "array",
    "boolean",
    "break",
    "byte",
    "case",
    "catch",
    "class",
    "colvector",
    "complex",
    "const",
    "continue",
    "default",
    "delegate",
    "delete",
    "do",
    "double",
    "else",
    "eltypedef",
    "end",
    "enum",
    "explicit",
    "export",
    "external",
    "float",
    "for",
    "friend",
    "function",
    "global",
    "goto",
    "if",
    "inline",
    "int",
    "local",
    "long",
    "NULL",
    "pragma",
    "protected",
    "quad",
    "rowvector",
    "short",
    "typedef",
    "typename",
    "virtual",
    "_all",
    "_N",
    "_skip",
    "_b",
    "_pi",
    "str#",
    "in",
    "_pred",
    "strL",
    "_coef",
    "_rc",
    "using",
    "_cons",
    "_se",
    "with",
    "_n",
)
