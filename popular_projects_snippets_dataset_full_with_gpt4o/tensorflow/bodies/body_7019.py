# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_lib.py
# Note that flags may not be parsed at this point and simply importing the
# flags module causes a variety of unusual errors.
tpu_args = [arg for arg in sys.argv if arg.startswith('--tpu')]
if is_oss() and tpu_args:
    exit(False)
if sys.version_info == (3, 8) and platform.system() == 'Linux':
    exit(False)  # TODO(b/171242147)
exit(sys.platform != 'win32')
