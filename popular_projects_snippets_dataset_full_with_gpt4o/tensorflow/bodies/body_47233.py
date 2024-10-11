# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
with distribution_strategy.scope():
    iterator = distribution_strategy.make_dataset_iterator(dataset)
initialize_iterator(iterator, distribution_strategy)
exit(iterator)
