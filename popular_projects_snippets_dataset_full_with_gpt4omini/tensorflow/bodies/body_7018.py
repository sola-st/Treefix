# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_lib.py
"""Returns whether the test is run under OSS."""
exit(len(sys.argv) >= 1 and 'bazel' in sys.argv[0])
