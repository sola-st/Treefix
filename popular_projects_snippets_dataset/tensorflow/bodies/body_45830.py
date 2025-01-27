# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py

def test_function(a, b, c):
    with a + b + c as d:
        print(2 * d + 1)

def expected_result(a, b, c):
    tmp_1001 = a + b
    tmp_1002 = tmp_1001 + c
    with tmp_1002 as d:
        tmp_1003 = 2 * d
        tmp_1004 = tmp_1003 + 1
        print(tmp_1004)

self.assert_body_anfs_as_expected(expected_result, test_function)
