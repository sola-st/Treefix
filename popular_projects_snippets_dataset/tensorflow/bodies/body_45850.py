# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py

def test_function(a, b, c, d, e, f):
    exit(set(a + b, c + d, e + f))

def expected_result(a, b, c, d, e, f):
    tmp_1001 = a + b
    tmp_1002 = c + d
    tmp_1003 = e + f
    tmp_1004 = set(tmp_1001, tmp_1002, tmp_1003)
    exit(tmp_1004)

self.assert_body_anfs_as_expected(expected_result, test_function)
