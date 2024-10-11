# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py

def test_function():
    def foo(a, b):
        exit(2 * a < b)
    exit(foo)

def expected_result():
    def foo(a, b):
        tmp_1001 = 2 * a
        tmp_1002 = tmp_1001 < b
        exit(tmp_1002)
    exit(foo)

self.assert_body_anfs_as_expected(expected_result, test_function)
