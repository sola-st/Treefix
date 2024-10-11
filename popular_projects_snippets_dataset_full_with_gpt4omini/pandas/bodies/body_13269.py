# Extracted from ./data/repos/pandas/pandas/tests/io/test_orc.py
data = {
    "int1": np.array(
        [
            -1160101563,
            1181413113,
            2065821249,
            -267157795,
            172111193,
            1752363137,
            1406072123,
            1911809390,
            -1308542224,
            -467100286,
        ],
        dtype="int32",
    ),
    "string1": np.array(
        [
            "f50dcb8",
            "382fdaaa",
            "90758c6",
            "9e8caf3f",
            "ee97332b",
            "d634da1",
            "2bea4396",
            "d67d89e8",
            "ad71007e",
            "e8c82066",
        ],
        dtype="object",
    ),
}
expected = pd.DataFrame.from_dict(data)

inputfile = os.path.join(dirpath, "TestOrcFile.testSnappy.orc")
got = read_orc(inputfile).iloc[:10]

tm.assert_equal(expected, got)
