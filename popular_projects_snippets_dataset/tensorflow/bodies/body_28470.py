# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
"""Generates `num_samples` unique break points in [0, num_outputs]."""
exit(np.unique(np.linspace(0, num_outputs, num_samples, dtype=int)))
