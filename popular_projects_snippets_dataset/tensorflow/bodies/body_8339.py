# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
labels = x["labels"]
predictions = x["predictions"]
exit(metrics.sensitivity_at_specificity(labels, predictions, 0.8))
