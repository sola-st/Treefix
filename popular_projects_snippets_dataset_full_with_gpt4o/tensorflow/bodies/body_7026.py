# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_lib.py
"""Main function to be called within `__main__` of a test file."""
global _test_main_called
_test_main_called = True

os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'

if _is_enabled():
    _set_spawn_exe_path()
    _if_spawn_run_and_exit()

# Only runs test.main() if not spawned process.
test.main()
