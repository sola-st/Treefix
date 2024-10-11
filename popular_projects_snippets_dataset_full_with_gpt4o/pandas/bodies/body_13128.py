# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_style.py
# GH#46381

mock_bucket_name, target_file = "pandas-test", "test.xlsx"
df = DataFrame({"x": [1, 2, 3], "y": [2, 4, 6]})
styler = df.style.set_sticky(axis="index")
styler.to_excel(f"s3://{mock_bucket_name}/{target_file}", storage_options=s3so)
timeout = 5
while True:
    if target_file in (
        obj.key for obj in s3_resource.Bucket("pandas-test").objects.all()
    ):
        break
    time.sleep(0.1)
    timeout -= 0.1
    assert timeout > 0, "Timed out waiting for file to appear on moto"
    result = read_excel(
        f"s3://{mock_bucket_name}/{target_file}", index_col=0, storage_options=s3so
    )
    tm.assert_frame_equal(result, df)
