# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_arrays_v1.py
if distribution_strategy:
    distributed_training_utils_v1.initialize_iterator(
        iterator, distribution_strategy)
else:
    training_utils_v1.initialize_iterator(iterator)
