# Extracted from ./data/repos/pandas/pandas/tests/io/test_orc.py
data = {
    "time": np.array(
        [
            "1900-05-05 12:34:56.100000",
            "1900-05-05 12:34:56.100100",
            "1900-05-05 12:34:56.100200",
            "1900-05-05 12:34:56.100300",
            "1900-05-05 12:34:56.100400",
            "1900-05-05 12:34:56.100500",
            "1900-05-05 12:34:56.100600",
            "1900-05-05 12:34:56.100700",
            "1900-05-05 12:34:56.100800",
            "1900-05-05 12:34:56.100900",
        ],
        dtype="datetime64[ns]",
    ),
    "date": np.array(
        [
            datetime.date(1900, 12, 25),
            datetime.date(1900, 12, 25),
            datetime.date(1900, 12, 25),
            datetime.date(1900, 12, 25),
            datetime.date(1900, 12, 25),
            datetime.date(1900, 12, 25),
            datetime.date(1900, 12, 25),
            datetime.date(1900, 12, 25),
            datetime.date(1900, 12, 25),
            datetime.date(1900, 12, 25),
        ],
        dtype="object",
    ),
}
expected = pd.DataFrame.from_dict(data)

inputfile = os.path.join(dirpath, "TestOrcFile.testDate1900.orc")
got = read_orc(inputfile).iloc[:10]

tm.assert_equal(expected, got)
