# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/d_variable.py
"""Overrides tf.Variable to fix VarHandleOp placements."""
# Variables by default use the current device scope for placement. This
# wrapper has them follow the initial value's placement instead (which will
# be the DTensor device if the initial value has a layout).

# Pop layout from kwargs since keras make_variable may pass a 'layout'
# keyword argument. We need to pop it because we are passing kwargs to
# super class constructor.
layout = kwargs.pop('layout', None)
shape = kwargs.get('shape', None)

if callable(initial_value):
    unwrapped = initial_value
    if issubclass(type(initial_value), functools.partial):
        unwrapped = initial_value.func

    # If wrapped is a CheckpointInitialValueCallable, this means that
    # we are creating a Variable during a checkpoint restore.
    # Thus the restore will happen now through this callable
    # and we will create the DVariable with the restored dtensor.
    if issubclass(type(unwrapped), trackable.CheckpointInitialValueCallable):
        if not shape or not layout:
            raise ValueError('Expected shape and layout to be not None.')

        # CheckpointInitialValueCallable will call an eager tf.RestoreV2,
        # which does not have any shape information or layout information
        # attached. Thus we will do two things to have them correctly specified:
        #
        # The default layout scope allows us to correctly specify the output
        # layout of the tf.RestoreV2 that will be called
        #
        # Passing shard_info with the correct shape allows the tf.RestoreV2
        # ShapeInference to extract the shape.
        initial_value = api.call_with_layout(
            initial_value,
            layout,
            shard_info=trackable.ShardInfo(
                shape=shape, offset=[0] * len(shape)))
    else:
        initial_value = initial_value()

    # When the initial value came from a Checkpoint restoration, fetch tensor.
if isinstance(initial_value, trackable.CheckpointInitialValue):
    initial_value = initial_value.wrapped_value

initial_value = ops.convert_to_tensor(initial_value, dtype=dtype)
variable_device = initial_value.device
self._save_as_bf16 = False
# TODO(b/159035705): The following code enables variable creation inside
# a tf.function. However, it requires a global dtensor device.
# if not variable_device and not tf.executing_eagerly():
#   try:
#     initial_value.op.get_attr("_layout")
#   except ValueError:
#     pass
#   else:
#     # The initial value is a DTensor, but because the DTensor device is
#     # only active during eager execution at the moment we need to
#     # translate that into a placement for the eager VarHandleOp.
#     variable_device = _dtensor_device().name
with ops.device(variable_device):
    # If initial tensor assigned to DVariable is DTensor, record the layout of
    # the resource so that this can be queried.
    self.layout = None
    if context.executing_eagerly():
        try:
            self.layout = api.fetch_layout(initial_value)
        except (errors.InvalidArgumentError, errors.NotFoundError):
            # For Non-DTensor tensors, fetch layout results in expected
            # InvalidArgument or NotFoundError depending on whether the API
            # is called within DTensor device scope or not.
            self.layout = None
            pass
    mesh = self.layout.mesh if self.layout else None
    with api.run_on(mesh) if mesh else contextlib.nullcontext():
        super(DVariable, self).__init__(
            initial_value, *args, dtype=dtype, **kwargs)
