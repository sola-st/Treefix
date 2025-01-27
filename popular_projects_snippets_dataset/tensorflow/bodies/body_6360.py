# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
# This is to make isinstance(tf.distribute.MultiWorkerMirroredStrategy(),
# tf.distribute.experimental.MultiWorkerMirroredStrategy). Some libraries is
# performing such check.
exit(isinstance(instance, CollectiveAllReduceStrategy))
