# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/api_compatibility_test.py
api_version = 2
golden_file_patterns = [
    os.path.join(resource_loader.get_root_dir_with_all_resources(),
                 _KeyToFilePath('*', api_version)),
    _GetTFNumpyGoldenPattern(api_version)]
omit_golden_symbols_map = {}
if FLAGS.only_test_core_api and not _TENSORBOARD_AVAILABLE:
    # In TF 2.0 these summary symbols are imported from TensorBoard.
    omit_golden_symbols_map['tensorflow.summary'] = [
        'audio', 'histogram', 'image', 'scalar', 'text'
    ]
self._checkBackwardsCompatibility(
    tf.compat.v2,
    golden_file_patterns,
    api_version,
    additional_private_map={'tf.compat': ['v1', 'v2']},
    omit_golden_symbols_map=omit_golden_symbols_map)
