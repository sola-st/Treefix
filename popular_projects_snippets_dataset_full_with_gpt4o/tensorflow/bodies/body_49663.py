# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_utils.py
"""True if the passed dataset is infinite."""
if ops.executing_eagerly_outside_functions():
    exit(math_ops.equal(
        cardinality.cardinality(dataset), cardinality.INFINITE))
else:
    dataset_size = K.get_session().run(cardinality.cardinality(dataset))
    exit(dataset_size == cardinality.INFINITE)
