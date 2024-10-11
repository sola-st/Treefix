# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/api_compatibility_test.py
api_version = 1
golden_file_patterns = os.path.join(
    resource_loader.get_root_dir_with_all_resources(),
    _KeyToFilePath('*', api_version))
self._checkBackwardsCompatibility(
    tf.compat.v1,
    golden_file_patterns,
    api_version,
    additional_private_map={
        'tf': ['pywrap_tensorflow'],
        'tf.compat': ['v1', 'v2'],
    },
    omit_golden_symbols_map={'tensorflow': ['pywrap_tensorflow']})
