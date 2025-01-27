# Extracted from ./data/repos/pandas/pandas/tests/io/test_orc.py
data = {
    "time": np.array(
        [
            "2038-05-05 12:34:56.100000",
            "2038-05-05 12:34:56.100100",
            "2038-05-05 12:34:56.100200",
            "2038-05-05 12:34:56.100300",
            "2038-05-05 12:34:56.100400",
            "2038-05-05 12:34:56.100500",
            "2038-05-05 12:34:56.100600",
            "2038-05-05 12:34:56.100700",
            "2038-05-05 12:34:56.100800",
            "2038-05-05 12:34:56.100900",
        ],
        dtype="datetime64[ns]",
    ),
    "date": np.array(
        [
            datetime.date(2038, 12, 25),
            datetime.date(2038, 12, 25),
            datetime.date(2038, 12, 25),
            datetime.date(2038, 12, 25),
            datetime.date(2038, 12, 25),
            datetime.date(2038, 12, 25),
            datetime.date(2038, 12, 25),
            datetime.date(2038, 12, 25),
            datetime.date(2038, 12, 25),
            datetime.date(2038, 12, 25),
        ],
        dtype="object",
    ),
}
expected = pd.DataFrame.from_dict(data)

inputfile = os.path.join(dirpath, "TestOrcFile.testDate2038.orc")
got = read_orc(inputfile).iloc[:10]

tm.assert_equal(expected, got)
