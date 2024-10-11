# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH 28375
mock_bucket_name, target_file = "pandas-test", "test.json"
df = DataFrame({"x": [1, 2, 3], "y": [2, 4, 6]})
df.to_json(f"s3://{mock_bucket_name}/{target_file}", storage_options=s3so)
timeout = 5
while True:
    if target_file in (
        obj.key for obj in s3_resource.Bucket("pandas-test").objects.all()
    ):
        break
    time.sleep(0.1)
    timeout -= 0.1
    assert timeout > 0, "Timed out waiting for file to appear on moto"
