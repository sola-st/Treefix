# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py

def test_function(b, c, d, f):
    a = c + d
    a.b = c + d
    a[b] = c + d
    a += c + d
    a, b = c
    a, b = c, d
    a = f(c)
    a = f(c + d)
    a[b + d] = f.e(c + d)

def expected_result(b, c, d, f):
    a = c + d
    a.b = c + d  # Should be a.b = tmp?  (Definitely not tmp = c + d)
    a[b] = c + d  # Should be a[b] = tmp?  (Definitely not tmp = c + d)
    a += c + d  # Should be a += tmp?  (Definitely not tmp = c + d)
    a, b = c  # Should be a = c[0], b = c[1]?  Or not?
    a, b = c, d  # Should be a = c, b = d?  Or not?
    a = f(c)
    tmp_1001 = c + d
    a = f(tmp_1001)
    tmp_1002 = b + d
    tmp_1003 = f.e
    tmp_1004 = c + d
    a[tmp_1002] = tmp_1003(tmp_1004)  # Or should be a[tmp1] = tmp2?

self.assert_body_anfs_as_expected(expected_result, test_function)
