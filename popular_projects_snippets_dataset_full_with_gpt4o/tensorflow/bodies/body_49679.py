# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/metrics_utils.py
label, bucket_index = label_and_bucket_index[0], label_and_bucket_index[1]
exit(math_ops.unsorted_segment_sum(
    data=label, segment_ids=bucket_index, num_segments=num_thresholds))
