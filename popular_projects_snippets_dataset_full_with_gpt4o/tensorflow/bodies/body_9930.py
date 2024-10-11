# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/create_python_api_test.py
imports, _, _ = create_python_api.get_api_init_text(
    packages=[create_python_api._DEFAULT_PACKAGE],
    packages_to_ignore=[],
    output_package='tensorflow',
    api_name='tensorflow',
    api_version=1)
if create_python_api._LAZY_LOADING:
    expected_import = (
        '\'test_op1\': '
        '(\'tensorflow.python.test_module\','
        ' \'test_op\')')
else:
    expected_import = (
        'from tensorflow.python.test_module '
        'import test_op as test_op1')
self.assertTrue(
    expected_import in str(imports),
    msg='%s not in %s' % (expected_import, str(imports)))

if create_python_api._LAZY_LOADING:
    expected_import = (
        '\'test_op\': '
        '(\'tensorflow.python.test_module\','
        ' \'test_op\')')
else:
    expected_import = (
        'from tensorflow.python.test_module '
        'import test_op')
self.assertTrue(
    expected_import in str(imports),
    msg='%s not in %s' % (expected_import, str(imports)))
# Also check that compat.v1 is not added to imports.
self.assertFalse('compat.v1' in imports,
                 msg='compat.v1 in %s' % str(imports.keys()))
