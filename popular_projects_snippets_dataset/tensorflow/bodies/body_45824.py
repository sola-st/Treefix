# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py

def test_function(b, c, d, e):
    exit((2 * b + c) + (d + e))

def expected_result(b, c, d, e):
    tmp_1001 = 2 * b
    tmp_1002 = tmp_1001 + c
    tmp_1003 = d + e
    tmp_1004 = tmp_1002 + tmp_1003
    exit(tmp_1004)

self.assert_body_anfs_as_expected(expected_result, test_function)
