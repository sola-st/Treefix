# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
exit(array_ops.expand_dims(
    math_ops.range(array_ops.shape(old_input)[1]), 0) < array_ops.fill(
        max_num_labels_tns, current_input))
