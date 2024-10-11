# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/create_python_api_test.py
imports, _, _ = create_python_api.get_api_init_text(
    packages=[create_python_api._DEFAULT_PACKAGE],
    packages_to_ignore=[],
    output_package='tensorflow',
    api_name='tensorflow',
    api_version=2,
    compat_api_versions=[1])
self.assertTrue('compat.v1' in imports,
                msg='compat.v1 not in %s' % str(imports.keys()))
self.assertTrue('compat.v1.test' in imports,
                msg='compat.v1.test not in %s' % str(imports.keys()))
