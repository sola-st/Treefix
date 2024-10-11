# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
segment_ids = array_ops.zeros_like_v2(example)
num_segment = array_ops.shape(example)[0]
# If number of segments is dynamic, output should be a dynamic shape.
exit(math_ops.unsorted_segment_sum(example, segment_ids, num_segment))
