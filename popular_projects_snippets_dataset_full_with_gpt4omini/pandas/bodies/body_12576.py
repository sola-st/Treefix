# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
index = pd.date_range("20000101", periods=10, freq="H")
# freq doesn't round-trip
index = DatetimeIndex(list(index), freq=None)

df_mixed = DataFrame(
    {
        "float_1": [
            -0.92077639,
            0.77434435,
            1.25234727,
            0.61485564,
            -0.60316077,
            0.24653374,
            0.28668979,
            -2.51969012,
            0.95748401,
            -1.02970536,
        ],
        "int_1": [
            19680418,
            75337055,
            99973684,
            65103179,
            79373900,
            40314334,
            21290235,
            4991321,
            41903419,
            16008365,
        ],
        "str_1": [
            "78c608f1",
            "64a99743",
            "13d2ff52",
            "ca7f4af2",
            "97236474",
            "bde7e214",
            "1a6bde47",
            "b1190be5",
            "7a669144",
            "8d64d068",
        ],
        "float_2": [
            -0.0428278,
            -1.80872357,
            3.36042349,
            -0.7573685,
            -0.48217572,
            0.86229683,
            1.08935819,
            0.93898739,
            -0.03030452,
            1.43366348,
        ],
        "str_2": [
            "14f04af9",
            "d085da90",
            "4bcfac83",
            "81504caf",
            "2ffef4a9",
            "08e2f5c4",
            "07e1af03",
            "addbd4a7",
            "1f6a09ba",
            "4bfc4d87",
        ],
        "int_2": [
            86967717,
            98098830,
            51927505,
            20372254,
            12601730,
            20884027,
            34193846,
            10561746,
            24867120,
            76131025,
        ],
    },
    index=index,
)

# JSON deserialisation always creates unicode strings
df_mixed.columns = df_mixed.columns.astype("unicode")

df_roundtrip = read_json(df_mixed.to_json(orient="split"), orient="split")
tm.assert_frame_equal(
    df_mixed,
    df_roundtrip,
    check_index_type=True,
    check_column_type=True,
    by_blocks=True,
    check_exact=True,
)
