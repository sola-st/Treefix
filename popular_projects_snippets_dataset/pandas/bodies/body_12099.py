# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_network.py
# see gh-16135

s3_object = s3_resource.meta.client.get_object(
    Bucket="pandas-test", Key="tips.csv"
)

with BytesIO(s3_object["Body"].read()) as buffer:
    result = read_csv(buffer, encoding="utf8")
assert isinstance(result, DataFrame)
assert not result.empty

expected = read_csv(tips_file)
tm.assert_frame_equal(result, expected)
