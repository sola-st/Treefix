# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py

def test_function(a, b, c, d, e, f):
    a[b][c] = d[e][f] + 3

def expected_result(a, b, c, d, e, f):
    tmp_1001 = a[b]
    tmp_1002 = d[e]
    tmp_1003 = tmp_1002[f]
    tmp_1001[c] = tmp_1003 + 3

self.assert_body_anfs_as_expected(expected_result, test_function)
