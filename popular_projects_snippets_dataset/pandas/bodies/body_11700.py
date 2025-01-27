# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_file_buffer_url.py
parser = all_parsers
df = tm.makeDataFrame()
result = tm.round_trip_localpath(
    df.to_csv, lambda p: parser.read_csv(p, index_col=0)
)
tm.assert_frame_equal(df, result)
