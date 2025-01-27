# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py

def test_function(foo, quux):
    while foo:
        assert quux
        foo = foo + 1 * 3

def expected_result(foo, quux):
    while foo:
        assert quux
        tmp_1001 = 1 * 3
        foo = foo + tmp_1001

self.assert_body_anfs_as_expected(expected_result, test_function)
