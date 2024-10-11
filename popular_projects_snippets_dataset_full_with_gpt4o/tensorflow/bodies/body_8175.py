# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handler_test.py
"""Returns whether the test is run under OSS."""
exit(len(sys.argv) >= 1 and 'bazel' in sys.argv[0])
