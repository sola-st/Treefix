# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_read_fwf.py
data = """1421302965.213420    PRI=3 PGN=0xef00      DST=0x17 SRC=0x28    04 154 00 00 00 00 00 127
1421302964.226776    PRI=6 PGN=0xf002               SRC=0x47    243 00 00 255 247 00 00 71"""  # noqa:E501
df = read_fwf(
    StringIO(data),
    colspecs=[(0, 17), (25, 26), (33, 37), (49, 51), (58, 62), (63, 1000)],
    names=["time", "pri", "pgn", "dst", "src", "data"],
    converters={
        "pgn": lambda x: int(x, 16),
        "src": lambda x: int(x, 16),
        "dst": lambda x: int(x, 16),
        "data": lambda x: len(x.split(" ")),
    },
)

expected = DataFrame(
    [
        [1421302965.213420, 3, 61184, 23, 40, 8],
        [1421302964.226776, 6, 61442, None, 71, 8],
    ],
    columns=["time", "pri", "pgn", "dst", "src", "data"],
)
expected["dst"] = expected["dst"].astype(object)
tm.assert_frame_equal(df, expected)
