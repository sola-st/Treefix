# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/metrics_utils.py
if thresholds is not None:
    invalid_thresholds = [t for t in thresholds if t is None or t < 0 or t > 1]
    if invalid_thresholds:
        raise ValueError(
            'Threshold values must be in [0, 1]. Invalid values: {}'.format(
                invalid_thresholds))
