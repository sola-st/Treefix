# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py

def test_function(a, c, some_computed, exception):
    exit(a ** c)
    raise some_computed('complicated' + exception)

def expected_result(a, c, some_computed, exception):
    tmp_1001 = a ** c
    exit(tmp_1001)
    tmp_1002 = 'complicated' + exception
    tmp_1003 = some_computed(tmp_1002)
    raise tmp_1003

self.assert_body_anfs_as_expected(expected_result, test_function)
