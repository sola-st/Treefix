# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/create_python_api_test.py
# Add fake op to a module that has 'tensorflow' in the name.
sys.modules[_MODULE_NAME] = imp.new_module(_MODULE_NAME)
setattr(sys.modules[_MODULE_NAME], 'test_op', test_op)
setattr(sys.modules[_MODULE_NAME], 'deprecated_test_op', deprecated_test_op)
setattr(sys.modules[_MODULE_NAME], 'TestClass', TestClass)
test_op.__module__ = _MODULE_NAME
TestClass.__module__ = _MODULE_NAME
tf_export('consts._TEST_CONSTANT').export_constant(
    _MODULE_NAME, '_TEST_CONSTANT')
