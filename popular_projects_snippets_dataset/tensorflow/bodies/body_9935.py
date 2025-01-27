# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/create_python_api_test.py
save_dir = self.get_temp_dir()
proxy_module_root = 'keras.api._v2'
module = 'keras.losses'
module_dir = module.replace('.', '/')
proxy_file = os.path.join(save_dir, module_dir, '__init__.py')
expected_imports = [f'from {proxy_module_root}.{module} import *']
create_python_api.create_proxy_api_files([proxy_file],
                                         proxy_module_root,
                                         save_dir)
self.assertTrue(os.path.exists(proxy_file))
with open(proxy_file, 'r') as f:
    lines = f.readlines()
self.assertCountEqual(expected_imports, lines)
