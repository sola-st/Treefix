# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/input_layer.py
self._init_input_shape = input_shape
self._init_batch_size = batch_size
self._init_dtype = dtype
self._init_sparse = sparse
self._init_ragged = ragged
self._init_type_spec = type_spec

strategy = distribution_strategy_context.get_strategy()
if strategy and batch_size is not None and \
        distributed_training_utils.global_batch_size_supported(strategy):
    if batch_size % strategy.num_replicas_in_sync != 0:
        raise ValueError('The `batch_size` argument ({}) must be divisible by '
                         'the number of replicas ({})'.format(
                             batch_size, strategy.num_replicas_in_sync))
    batch_size = batch_size // strategy.num_replicas_in_sync

if 'batch_input_shape' in kwargs:
    batch_input_shape = kwargs.pop('batch_input_shape')
    if input_shape and batch_input_shape:
        raise ValueError('Only provide the input_shape OR '
                         'batch_input_shape argument to '
                         'InputLayer, not both at the same time.')
    # Set the input shape and batch size from the batch_input_shape.
    # Note that batch_input_shape can be None (unknown rank) or [] (scalar),
    # in which case the batch size must be None.
    if batch_input_shape:
        batch_size = batch_input_shape[0]
        input_shape = batch_input_shape[1:]
if kwargs:
    raise ValueError('Unrecognized keyword arguments:', kwargs.keys())

if sparse and ragged:
    raise ValueError(
        'Cannot set both sparse and ragged to True in a Keras input.')

if not name:
    prefix = 'input'
    name = prefix + '_' + str(backend.get_uid(prefix))

if not dtype:
    if input_tensor is None:
        dtype = backend.floatx()
    else:
        dtype = backend.dtype(input_tensor)
elif input_tensor is not None and input_tensor.dtype != dtype:
    raise ValueError('`input_tensor.dtype` differs from `dtype`: %s vs. %s' %
                     (input_tensor.dtype, dtype))
super(InputLayer, self).__init__(dtype=dtype, name=name)
self.built = True
self.sparse = True if sparse else False
self.ragged = True if ragged else False
self.batch_size = batch_size
self.supports_masking = True

if isinstance(input_shape, tensor_shape.TensorShape):
    input_shape = tuple(input_shape.as_list())
elif isinstance(input_shape, int):
    input_shape = (input_shape,)

if type_spec is not None:
    args_that_must_be_none = [
        ('(input_)shape', self._init_input_shape),
        ('batch_size', self._init_batch_size),
        ('dtype', self._init_dtype),
        ('input_tensor', input_tensor),
        ('sparse', self._init_sparse),
        ('ragged', self._init_ragged),
    ]
    for arg_name, arg in args_that_must_be_none:
        _assert_other_arg_none(arg_name, arg)
    if not ops.executing_eagerly_outside_functions():
        raise ValueError('Creating Keras inputs from a type_spec is only '
                         'supported when eager execution is enabled.')
    input_tensor = keras_tensor.keras_tensor_from_type_spec(type_spec)
    if isinstance(input_tensor, keras_tensor.SparseKerasTensor):
        self.sparse = True
    if isinstance(input_tensor, keras_tensor.RaggedKerasTensor):
        self.ragged = True
    self.is_placeholder = True
    try:
        self._batch_input_shape = tuple(input_tensor.shape.as_list())
    except ValueError:
        # If the shape cannot be represented as a tuple (e.g. unknown rank)
        self._batch_input_shape = None
elif input_tensor is None:
    if input_shape is not None:
        batch_input_shape = (batch_size,) + tuple(input_shape)
    else:
        batch_input_shape = None
    graph = backend.get_graph()
    with graph.as_default():
        input_tensor = backend.placeholder(
            shape=batch_input_shape,
            dtype=dtype,
            name=self.name,
            sparse=sparse,
            ragged=ragged)

    self.is_placeholder = True
    self._batch_input_shape = batch_input_shape
else:
    if ops.executing_eagerly_outside_functions():
        if not isinstance(input_tensor, keras_tensor.KerasTensor):
            input_tensor = keras_tensor.keras_tensor_from_tensor(input_tensor)
    else:
        if not tf_utils.is_symbolic_tensor(input_tensor):
            raise ValueError('You should not pass an EagerTensor to `Input`. '
                             'For example, instead of creating an '
                             'InputLayer, you should instantiate your model and '
                             'directly call it on your input.')
    self.is_placeholder = False
    try:
        self._batch_input_shape = tuple(input_tensor.shape.as_list())
    except ValueError:
        # If the shape cannot be represented as a tuple (e.g. unknown rank)
        self._batch_input_shape = None
    # Create an input node.
input_tensor._keras_mask = None
node_module.Node(layer=self, outputs=input_tensor)

# Store type spec
if isinstance(input_tensor, keras_tensor.KerasTensor) or (
    tf_utils.is_extension_type(input_tensor)):
    self._type_spec = input_tensor._type_spec  # pylint: disable=protected-access
else:
    self._type_spec = tensor_spec.TensorSpec(
        shape=input_tensor.shape, dtype=input_tensor.dtype, name=self.name)
