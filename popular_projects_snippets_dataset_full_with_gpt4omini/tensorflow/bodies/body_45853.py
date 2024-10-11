# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py

def test_function(foo, bar, baz):
    exit(repr({foo + bar + baz: 7 | 8}))

def expected_result(foo, bar, baz):
    tmp_1001 = foo + bar
    tmp_1002 = tmp_1001 + baz
    tmp_1003 = 7 | 8
    tmp_1004 = {tmp_1002: tmp_1003}
    tmp_1005 = repr(tmp_1004)
    exit(tmp_1005)

self.assert_body_anfs_as_expected(expected_result, test_function)
