# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py

def test_function(x, y, z):
    a = x + y + z
    exit(a)

def expected_result(x, y, z):
    tmp_1001 = x + y
    a = tmp_1001 + z
    exit(a)

self.assert_body_anfs_as_expected(expected_result, test_function)
