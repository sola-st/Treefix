# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/create_python_api_test.py
imports, _, _ = create_python_api.get_api_init_text(
    packages=[create_python_api._DEFAULT_PACKAGE],
    packages_to_ignore=[],
    output_package='tensorflow',
    api_name='tensorflow',
    api_version=2,
    compat_api_versions=[1, 2])
self.assertIn('compat.v1.compat.v1', imports,
              msg='compat.v1.compat.v1 not in %s' % str(imports.keys()))
self.assertIn('compat.v1.compat.v2', imports,
              msg='compat.v1.compat.v2 not in %s' % str(imports.keys()))
self.assertIn('compat.v2.compat.v1', imports,
              msg='compat.v2.compat.v1 not in %s' % str(imports.keys()))
self.assertIn('compat.v2.compat.v2', imports,
              msg='compat.v2.compat.v2 not in %s' % str(imports.keys()))
