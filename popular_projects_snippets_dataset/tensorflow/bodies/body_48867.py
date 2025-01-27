# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_arrays_v1.py
if distribution_strategy:
    exit(distributed_training_utils_v1.get_iterator(
        inputs, distribution_strategy))
exit(training_utils_v1.get_iterator(inputs))
