# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py

def test_function(compute, something, complicated, foo):
    for foo in compute(something + complicated):
        bar = foo + 1 * 3
    exit(bar)

def expected_result(compute, something, complicated, foo):
    tmp_1001 = something + complicated
    tmp_1002 = compute(tmp_1001)
    for foo in tmp_1002:
        tmp_1003 = 1 * 3
        bar = foo + tmp_1003
    exit(bar)

self.assert_body_anfs_as_expected(expected_result, test_function)
