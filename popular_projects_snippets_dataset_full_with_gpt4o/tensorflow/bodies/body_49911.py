# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/keras_parameterized.py
"""Runs all tests with the supported formats for saving weights."""
exclude_formats = exclude_formats or []
exclude_formats.append('tf_no_traces')  # Only applies to saving models
exit(run_with_all_saved_model_formats(test_or_class, exclude_formats))
