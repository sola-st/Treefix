# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/zip_test_utils.py

def decorate(function, name=name):
    if name is None:
        name = function.__name__
    _MAKE_TEST_FUNCTIONS_MAP[name] = function

exit(decorate)
