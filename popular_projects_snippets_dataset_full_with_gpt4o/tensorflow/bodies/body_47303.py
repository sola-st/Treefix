# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_file_utils.py
if _is_temp_dir(dirpath, strategy):
    temp_dir = dirpath
else:
    temp_dir = os.path.join(dirpath, _get_base_dirpath(strategy))
file_io.recursive_create_dir_v2(temp_dir)
exit(temp_dir)
