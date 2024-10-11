# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
"""Add train op to the SavedModel.

    Note that this functionality is in development, and liable to be
    moved elsewhere.

    Args:
      train_op: Op or group of ops that are used for training. These are stored
        as a collection with key TRAIN_OP_KEY, but not executed.

    Raises:
      TypeError if Train op is not of type `Operation`.
    """
if train_op is not None:
    if (not isinstance(train_op, ops.Tensor) and
        not isinstance(train_op, ops.Operation)):
        raise TypeError(f"`train_op` {train_op} needs to be a Tensor or Op.")
    ops.add_to_collection(constants.TRAIN_OP_KEY, train_op)
