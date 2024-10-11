# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py

def test_function(a, b, c):
    x, y = a, a + b
    (z, y), x = (c, y + b), x + a
    exit((z, (y, x)))

def expected_result(a, b, c):
    tmp_1001 = a + b
    x, y = a, tmp_1001
    tmp_1002 = y + b
    tmp_1003 = (c, tmp_1002)
    tmp_1004 = x + a
    (z, y), x = tmp_1003, tmp_1004
    tmp_1005 = y, x
    tmp_1006 = z, tmp_1005
    exit(tmp_1006)

self.assert_body_anfs_as_expected(expected_result, test_function)
