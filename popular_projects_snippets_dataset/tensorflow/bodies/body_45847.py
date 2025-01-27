# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py

def test_function(a, b, c, d, e, f):
    exit((a + b, -(c + d), e + f))

def expected_result(a, b, c, d, e, f):
    tmp_1001 = c + d
    tmp_1002 = a + b
    tmp_1003 = -tmp_1001
    tmp_1004 = e + f
    tmp_1005 = (tmp_1002, tmp_1003, tmp_1004)
    exit(tmp_1005)

self.assert_body_anfs_as_expected(expected_result, test_function)
