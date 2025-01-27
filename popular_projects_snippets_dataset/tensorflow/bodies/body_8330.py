# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
labels = x["labels"]
predictions = x["predictions"]
exit(metrics.recall_at_thresholds(labels, predictions, [0.5]))
