# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py

def test_function(a, b, c, e, f, g):
    if a + b + c:
        d = e + f + g
        exit(d)

def expected_result(a, b, c, e, f, g):
    tmp_1001 = a + b
    tmp_1002 = tmp_1001 + c
    if tmp_1002:
        tmp_1003 = e + f
        d = tmp_1003 + g
        exit(d)

self.assert_body_anfs_as_expected(expected_result, test_function)
