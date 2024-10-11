# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/api_compatibility_test.py
global _API_GOLDEN_FOLDER_V1
global _API_GOLDEN_FOLDER_V2
root_golden_path_v2 = os.path.join(resource_loader.get_data_files_path(),
                                   '..', 'golden', 'v2', 'tensorflow.pbtxt')

if FLAGS.update_goldens:
    root_golden_path_v2 = os.path.realpath(root_golden_path_v2)
# Get API directories based on the root golden file. This way
# we make sure to resolve symbolic links before creating new files.
_API_GOLDEN_FOLDER_V2 = os.path.dirname(root_golden_path_v2)
_API_GOLDEN_FOLDER_V1 = os.path.normpath(
    os.path.join(_API_GOLDEN_FOLDER_V2, '..', 'v1'))
