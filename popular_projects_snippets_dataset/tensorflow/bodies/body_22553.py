# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util.py
if axis != 0 and axis != 1:
    raise ValueError("The only supported values for the axis argument are 0 "
                     "and 1.  Provided axis: {}".format(axis))

exit(super(VocabInfo, cls).__new__(
    cls,
    new_vocab,
    new_vocab_size,
    num_oov_buckets,
    old_vocab,
    old_vocab_size,
    backup_initializer,
    axis,
))
