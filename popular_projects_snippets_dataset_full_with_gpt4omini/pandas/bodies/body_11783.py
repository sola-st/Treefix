# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
data = (
    '"09-Apr-2012", "01:10:18.300", 2456026.548822908, 12849, '
    "1.00361,  1.12551, 330.65659, 0355626618.16711,  73.48821, "
    "314.11625,  1917.09447,   179.71425,  80.000, 240.000, -350,  "
    "70.06056, 344.98370, 1,   1, -0.689265, -0.692787,  "
    "0.212036,    14.7674,   41.605,   -9999.0,   -9999.0,   "
    "-9999.0,   -9999.0,   -9999.0,  -9999.0, 000, 012, 128"
)
parser = all_parsers

result = parser.read_csv(
    StringIO(data),
    names=list(range(33)),
    header=None,
    na_values=["-9999.0"],
    skipinitialspace=True,
)
expected = DataFrame(
    [
        [
            "09-Apr-2012",
            "01:10:18.300",
            2456026.548822908,
            12849,
            1.00361,
            1.12551,
            330.65659,
            355626618.16711,
            73.48821,
            314.11625,
            1917.09447,
            179.71425,
            80.0,
            240.0,
            -350,
            70.06056,
            344.9837,
            1,
            1,
            -0.689265,
            -0.692787,
            0.212036,
            14.7674,
            41.605,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            0,
            12,
            128,
        ]
    ]
)
tm.assert_frame_equal(result, expected)
