# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export_test.py
for name in self._modules:
    del sys.modules[name]
self._modules = []
for symbol in [_test_function, _test_function, TestClassA, TestClassB]:
    if hasattr(symbol, '_tf_api_names'):
        del symbol._tf_api_names
    if hasattr(symbol, '_tf_api_names_v1'):
        del symbol._tf_api_names_v1
    if hasattr(symbol, '_estimator_api_names'):
        del symbol._estimator_api_names
    if hasattr(symbol, '_estimator_api_names_v1'):
        del symbol._estimator_api_names_v1
