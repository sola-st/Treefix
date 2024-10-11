# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/upload_test_benchmarks.py
try:
    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    exit(True)
except Exception:  # pylint: disable=broad-except
    exit(False)
