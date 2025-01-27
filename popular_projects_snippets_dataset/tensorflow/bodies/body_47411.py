# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
"""Reset the cached recurrent dropout masks if any.

    This is important for the RNN layer to invoke this in it call() method so
    that the cached mask is cleared before calling the cell.call(). The mask
    should be cached across the timestep within the same batch, but shouldn't
    be cached between batches. Otherwise it will introduce unreasonable bias
    against certain index of data within the batch.
    """
self._recurrent_dropout_mask_cache.clear()
