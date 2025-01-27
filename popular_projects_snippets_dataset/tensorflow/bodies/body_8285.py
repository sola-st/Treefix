# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
labels = x["labels"]
predictions = x["predictions"]
exit(metrics.mean_iou(
    labels, predictions, num_classes=5))
