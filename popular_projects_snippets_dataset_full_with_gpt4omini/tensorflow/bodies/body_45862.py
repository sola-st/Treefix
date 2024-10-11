# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py

def test_function(a, x, y, z):
    a += x + y + z
    del a
    del z[y][x]

def expected_result(a, x, y, z):
    tmp_1001 = x + y
    a += tmp_1001 + z
    del a
    tmp_1002 = z[y]
    del tmp_1002[x]

self.assert_body_anfs_as_expected(expected_result, test_function)
