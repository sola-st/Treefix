# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py

def test_function(foo, bar, function, quux, quozzle, w, x, y, z):
    with foo + bar:
        function(x + y)
    if quux + quozzle:
        function(z / w)

def expected_result(foo, bar, function, quux, quozzle, w, x, y, z):
    tmp_1001 = foo + bar
    with tmp_1001:
        tmp_1002 = x + y
        function(tmp_1002)
    tmp_1003 = quux + quozzle
    if tmp_1003:
        tmp_1004 = z / w
        function(tmp_1004)

self.assert_body_anfs_as_expected(expected_result, test_function)
