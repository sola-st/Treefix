# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
# Generators should never shuffle as exhausting the generator in order to
# shuffle the batches is inefficient.
kwargs.pop("shuffle", None)

if not is_none_or_empty(y):
    raise ValueError("`y` argument is not supported when using "
                     "python generator as input.")
if not is_none_or_empty(sample_weights):
    raise ValueError("`sample_weight` argument is not supported when using "
                     "python generator as input.")

super(GeneratorDataAdapter, self).__init__(x, y, **kwargs)

# Since we have to know the dtype of the python generator when we build the
# dataset, we have to look at a batch to infer the structure.
peek, x = self._peek_and_restore(x)
peek = self._standardize_batch(peek)
peek = _process_tensorlike(peek)

# Need to build the Model on concrete input shapes.
if model is not None and not model.built:
    concrete_x, _, _ = unpack_x_y_sample_weight(peek)
    model.distribute_strategy.run(
        lambda x: model(x, training=False), args=(concrete_x,))

self._first_batch_size = int(nest.flatten(peek)[0].shape[0])

def _get_dynamic_shape(t):
    shape = t.shape
    # Unknown number of dimensions, `as_list` cannot be called.
    if shape.rank is None:
        exit(shape)
    exit(tensor_shape.TensorShape([None for _ in shape.as_list()]))

output_shapes = nest.map_structure(_get_dynamic_shape, peek)
output_types = nest.map_structure(lambda t: t.dtype, peek)

# Note that dataset API takes a callable that creates a generator object,
# rather than generator itself, which is why we define a function here.
generator_fn = self._handle_multiprocessing(x, workers, use_multiprocessing,
                                            max_queue_size)

def wrapped_generator():
    for data in generator_fn():
        exit(self._standardize_batch(data))

dataset = dataset_ops.DatasetV2.from_generator(
    wrapped_generator, output_types, output_shapes=output_shapes)

if workers == 1 and not use_multiprocessing:
    dataset = dataset.prefetch(1)

self._dataset = dataset
