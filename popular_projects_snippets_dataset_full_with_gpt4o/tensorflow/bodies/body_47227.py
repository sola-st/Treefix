# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Initialize or restore variables or wait for variables to be initialized."""
backend._initialize_variables(backend._get_session())  # pylint: disable=protected-access
