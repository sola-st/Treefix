# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/create_python_api_test.py
imports, _, _ = create_python_api.get_api_init_text(
    packages=[create_python_api._DEFAULT_PACKAGE],
    packages_to_ignore=[],
    output_package='tensorflow',
    api_name='tensorflow',
    api_version=1)
if create_python_api._LAZY_LOADING:
    expected = ('\'_TEST_CONSTANT\':'
                ' (\'tensorflow.python.test_module\','
                ' \'_TEST_CONSTANT\')')
else:
    expected = ('from tensorflow.python.test_module '
                'import _TEST_CONSTANT')
self.assertTrue(expected in str(imports),
                msg='%s not in %s' % (expected, str(imports)))
