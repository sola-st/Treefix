# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_feed.py
"""Sets the shapes and types of the queue tuple elements.

    input_tensors is a list of Tensors whose types and shapes are used
    to set the queue configuration.

    Args:
      input_tensors: list of Tensors of the same types and shapes as
        the desired queue Tuple.

    Raises:
      ValueError: if input_tensors is not a list of length
        self.number_of_tuple_elements
    """
if len(input_tensors) != self.number_of_tuple_elements:
    raise ValueError(f"input_tensors is {str(input_tensors)}, but should be "
                     f"a list of {self.number_of_tuple_elements} Tensors")
self.set_tuple_shapes([t.shape for t in input_tensors])
self.set_tuple_types([t.dtype for t in input_tensors])
