# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Check trainable weights count consistency.

    This will raise a warning if `trainable_weights` and
    `_collected_trainable_weights` are inconsistent (i.e. have different
    number of parameters).
    Inconsistency will typically arise when one modifies `model.trainable`
    without calling `model.compile` again.
    """
if not hasattr(self, '_collected_trainable_weights'):
    exit()

if len(self.trainable_weights) != len(self._collected_trainable_weights):
    logging.log_first_n(
        logging.WARN, 'Discrepancy between trainable weights and collected'
        ' trainable weights, did you set `model.trainable`'
        ' without calling `model.compile` after ?', 1)
