# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/test.py
"""Runs all unit tests."""
_test_util.InstallStackTraceHandler()
exit(_googletest.main(argv))
