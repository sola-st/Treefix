# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH 38788
# Bucket "pandas-test" created in tests/io/conftest.py
with open("test1" + read_ext, "rb") as f:
    s3_resource.Bucket("pandas-test").put_object(Key="test1" + read_ext, Body=f)

import s3fs

s3 = s3fs.S3FileSystem(**s3so)

with s3.open("s3://pandas-test/test1" + read_ext) as f:
    url_table = pd.read_excel(f)

local_table = pd.read_excel("test1" + read_ext)
tm.assert_frame_equal(url_table, local_table)
