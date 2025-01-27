# Extracted from ./data/repos/pandas/pandas/tests/io/test_s3.py
# GH17135
# botocore gained iteration support in 1.10.47, can now be used in read_*
pytest.importorskip("botocore", minversion="1.10.47")
from botocore.response import StreamingBody

data = [b"foo,bar,baz\n1,2,3\n4,5,6\n", b"just,the,header\n"]
for el in data:
    body = StreamingBody(BytesIO(el), content_length=len(el))
    read_csv(body)
