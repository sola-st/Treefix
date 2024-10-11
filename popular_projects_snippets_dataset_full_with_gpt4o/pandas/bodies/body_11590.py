# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
# s3_resource hosts pandas-test
import s3fs

with pytest.raises(PermissionError, match="Access Denied"):
    fs = s3fs.S3FileSystem(anon=True)
    fs.ls("pandas-test")

    geom_df.to_xml("s3://pandas-test/geom.xml", compression="zip", parser=parser)
