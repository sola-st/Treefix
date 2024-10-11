# Extracted from ./data/repos/pandas/pandas/tests/io/conftest.py
for s3_key, file_name in test_s3_files:
    with open(file_name, "rb") as f:
        cli.put_object(Bucket=bucket_name, Key=s3_key, Body=f)
