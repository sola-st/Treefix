# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# Bucket "pandas-test" created in tests/io/conftest.py
with open("test1" + read_ext, "rb") as f:
    s3_resource.Bucket("pandas-test").put_object(Key="test1" + read_ext, Body=f)

url = "s3://pandas-test/test1" + read_ext

url_table = pd.read_excel(url, storage_options=s3so)
local_table = pd.read_excel("test1" + read_ext)
tm.assert_frame_equal(url_table, local_table)
