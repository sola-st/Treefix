# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
if not multi_process_lib.initialized():
    raise NotInitializedError(
        '`multi_process_runner` is not initialized. '
        'Please call `tf.__internal__.distribute.multi_process_runner.'
        'test_main()` within `if __name__ == \'__main__\':` block '
        'in your python module to properly initialize '
        '`multi_process_runner`.')
