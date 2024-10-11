# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
labels = x["labels"]
predictions = x["predictions"]
exit(metrics.true_negatives_at_thresholds(labels, predictions, [.5]))
