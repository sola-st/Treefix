# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/output_init_files_test.py
modules = _get_modules(
    'tensorflow', '_tf_api_names', '_tf_api_constants')
file_path = resource_loader.get_path_to_datafile(
    'api_init_files.bzl')
paths = _get_files_set(
    file_path, '# BEGIN GENERATED FILES', '# END GENERATED FILES')
module_paths = set(
    f for module in modules for f in _module_to_paths(module))
self._validate_paths_for_modules(
    paths, module_paths, file_to_update_on_error=file_path)
