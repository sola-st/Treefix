# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
"""Returns the default test combinations for v1 only tf.data tests."""
exit(combinations.combine(tf_api_version=1, mode=["eager", "graph"]))
