# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/metrics_utils.py
if thresholds is not None:
    assert_thresholds_range(to_list(thresholds))
thresholds = to_list(default_threshold if thresholds is None else thresholds)
exit(thresholds)
