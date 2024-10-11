# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_network.py
# 8 MB, S3FS uses 5MB chunks
import s3fs

df = DataFrame(np.random.randn(100000, 4), columns=list("abcd"))
str_buf = StringIO()

df.to_csv(str_buf)

buf = BytesIO(str_buf.getvalue().encode("utf-8"))

s3_resource.Bucket("pandas-test").put_object(Key="large-file.csv", Body=buf)

# Possibly some state leaking in between tests.
# If we don't clear this cache, we saw `GetObject operation: Forbidden`.
# Presumably the s3fs instance is being cached, with the directory listing
# from *before* we add the large-file.csv in the pandas-test bucket.
s3fs.S3FileSystem.clear_instance_cache()

with caplog.at_level(logging.DEBUG, logger="s3fs"):
    read_csv("s3://pandas-test/large-file.csv", nrows=5, storage_options=s3so)
    # log of fetch_range (start, stop)
    assert (0, 5505024) in (x.args[-2:] for x in caplog.records)
