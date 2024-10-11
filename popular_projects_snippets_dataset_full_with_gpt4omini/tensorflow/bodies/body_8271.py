# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
exit(dataset_ops.Dataset.from_tensor_slices({
    "labels": [1., .5, 1., 0.],
    "predictions": [1., .75, .25, 0.]}).repeat())
