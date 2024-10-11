# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Creates a representative dataset.

    Args:
      input_gen: A generator function that generates input samples for the
        model and has the same order, type and shape as the inputs to the model.
        Usually, this is a small subset of a few hundred samples randomly
        chosen, in no particular order, from the training or evaluation dataset.
    """
self.input_gen = input_gen
