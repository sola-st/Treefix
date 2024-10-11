# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_should_use_test.py
"""Temporarily reroute errors written to tf_logging.error into `captured`."""
with test.mock.patch.object(tf_should_use.tf_logging, 'error') as error:
    exit(error)
