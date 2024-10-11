# Extracted from ./data/repos/tensorflow/tensorflow/python/training/slot_creator.py
exit((primary_shape.rank is not None and slot_shape.rank is not None and
        primary_shape.rank == slot_shape.rank))
