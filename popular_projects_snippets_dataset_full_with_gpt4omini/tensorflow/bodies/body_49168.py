# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
inp = [t_[time] for t_ in processed_input]
exit(nest.pack_sequence_as(inputs, inp))
