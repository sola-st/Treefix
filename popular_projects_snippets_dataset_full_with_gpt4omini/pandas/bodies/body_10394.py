# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# 13046
data = """
    idx     A         ID3              DATETIME
    0   B-028  b76cd912ff "2014-10-08 13:43:27"
    1   B-054  4a57ed0b02 "2014-10-08 14:26:19"
    2   B-076  1a682034f8 "2014-10-08 14:29:01"
    3   B-023  b76cd912ff "2014-10-08 18:39:34"
    4   B-023  f88g8d7sds "2014-10-08 18:40:18"
    5   B-033  b76cd912ff "2014-10-08 18:44:30"
    6   B-032  b76cd912ff "2014-10-08 18:46:00"
    7   B-037  b76cd912ff "2014-10-08 18:52:15"
    8   B-046  db959faf02 "2014-10-08 18:59:59"
    9   B-053  b76cd912ff "2014-10-08 19:17:48"
    10  B-065  b76cd912ff "2014-10-08 19:21:38"
    """
df = pd.read_csv(
    StringIO(data), sep=r"\s+", index_col=[0], parse_dates=["DATETIME"]
)

result = df.groupby("ID3")["DATETIME"].transform(lambda x: x.diff())
assert is_timedelta64_dtype(result.dtype)

result = df[["ID3", "DATETIME"]].groupby("ID3").transform(lambda x: x.diff())
assert is_timedelta64_dtype(result.DATETIME.dtype)
