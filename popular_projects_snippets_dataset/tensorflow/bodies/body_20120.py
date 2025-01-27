# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_feed.py
"""Creates a new InfeedQueue with the given configuration.

    The configuration need not be fully specified at creation since it
    can be modified subsequently by methods that set the values
    explicitly or infer them from the shapes of inputs.

    Args:
      number_of_tuple_elements: the number of Tensors fed atomically through the
        queue, must be present unless it can be inferred from other arguments.
      tuple_types: if not None, a list of types of the elements of the queue.
      tuple_shapes: if not None, a list of shapes of the elements of the queue.
      shard_dimensions: if not None, a list of dimensions on which the
        elements of the queue should be sharded during automatic
        parallelization.
      number_of_partitions: if > 1, the infeed dequeue shape will contain
        the full shape that includes all partitions and add corresponding XLA
        annotation on the infeed dequeue op. In this case, the infeed is still
        data parallel that feeds per-core batch size to each core while the XLA
        computation may be partitioned. As XLA requires infeed dequeue shape to
        be per-replica shape, thus we need number_of_partitions here to
        calculate the per-replica unpartitioned shape.
      name: the name of the queue.

    Raises:
      ValueError: if number_of_tuple_elements <= 0; or
        number_of_tuple_arguments, tuple_types, tuple_shapes, and
        shard_dimensions are all None; or the length of tuple_types,
        tuple_shapes, or shard_dimensions is not equal to
        number_of_tuple_elements; or any element of shard_dimensions
        can't be converted to a Dimension.
      TypeError: if any element of tuple_types or tuple_shapes can't
        be converted to a dtype or TensorShape, respectively.
    """
self._frozen = False
self._generated_enqueue_ops = False
self._generated_dequeue_op = False
self._name = "InfeedQueue" if name is None else name
if number_of_partitions is None:
    self._number_of_partitions = 1
else:
    self._number_of_partitions = number_of_partitions
if number_of_tuple_elements is None:
    if tuple_types is not None:
        number_of_tuple_elements = len(tuple_types)
    elif tuple_shapes is not None:
        number_of_tuple_elements = len(tuple_shapes)
    elif shard_dimensions is not None:
        number_of_tuple_elements = len(shard_dimensions)
    else:
        raise ValueError(
            "number of tuple elements cannot be inferred from InfeedQueue "
            "constructor")
if number_of_tuple_elements <= 0:
    raise ValueError(f"number_of_tuple_elements {number_of_tuple_elements} "
                     "must be > 0")
# Make an empty sharding policy for each tuple element.
self._sharding_policies = [
    tpu_sharding.ShardingPolicy() for _ in range(number_of_tuple_elements)
]
if tuple_types is not None:
    self.set_tuple_types(tuple_types)
else:
    self._tuple_types = None
if tuple_shapes is not None:
    self.set_tuple_shapes(tuple_shapes)
else:
    self._tuple_shapes = None
if shard_dimensions is not None:
    self.set_shard_dimensions(shard_dimensions)
self._validate()
