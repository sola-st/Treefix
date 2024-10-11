# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py

def test_function(call_something, a, b, y, z, c, d, e, f, g, h, i):
    call_something(a + b, y * z, kwarg=c + d, *(e + f), **(g + h + i))

def expected_result(call_something, a, b, y, z, c, d, e, f, g, h, i):
    tmp_1001 = g + h
    tmp_1002 = a + b
    tmp_1003 = y * z
    tmp_1004 = e + f
    tmp_1005 = c + d
    tmp_1006 = tmp_1001 + i
    call_something(tmp_1002, tmp_1003, kwarg=tmp_1005, *tmp_1004, **tmp_1006)

self.assert_body_anfs_as_expected(expected_result, test_function)
