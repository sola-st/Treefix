# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
# First four batches of x: labels, predictions -> (labels == predictions)
#  0: 0, 0 -> True;   1: 1, 1 -> True;   2: 2, 2 -> True;   3: 3, 0 -> False
#  4: 4, 1 -> False;  5: 0, 2 -> False;  6: 1, 0 -> False;  7: 2, 1 -> False
#  8: 3, 2 -> False;  9: 4, 0 -> False; 10: 0, 1 -> False; 11: 1, 2 -> False
# 12: 2, 0 -> False; 13: 3, 1 -> False; 14: 4, 2 -> False; 15: 0, 0 -> True
exit(dataset_ops.Dataset.range(1000).map(
    lambda x: {"labels": x % 5, "predictions": x % 3}).batch(
        4, drop_remainder=True))
