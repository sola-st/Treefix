# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
input_t = array_ops.unstack(input_t)  # unstack for time_step dim
if go_backwards:
    input_t.reverse()
exit(input_t)
