# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
labels = x["labels"]
predictions = x["predictions"]
exit(metrics.auc(labels, predictions, num_thresholds=8, curve="PR",
                   summation_method="careful_interpolation"))
