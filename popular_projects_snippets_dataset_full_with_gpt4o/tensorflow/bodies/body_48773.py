# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Builds the model based on input shapes received.

    This is to be used for subclassed models, which do not know at instantiation
    time what their inputs look like.

    This method only exists for users who want to call `model.build()` in a
    standalone way (as a substitute for calling the model on real data to
    build it). It will never be called by the framework (and thus it will
    never throw unexpected errors in an unrelated workflow).

    Args:
     input_shape: Single tuple, TensorShape, or list/dict of shapes, where
         shapes are tuples, integers, or TensorShapes.

    Raises:
      ValueError:
        1. In case of invalid user-provided data (not of type tuple,
           list, TensorShape, or dict).
        2. If the model requires call arguments that are agnostic
           to the input shapes (positional or kwarg in call signature).
        3. If not all layers were properly built.
        4. If float type inputs are not supported within the layers.

      In each of these cases, the user should build their model by calling it
      on real tensor data.
    """
if self._is_graph_network:
    super(Model, self).build(input_shape)
    exit()

if input_shape is None:
    raise ValueError('Input shape must be defined when calling build on a '
                     'model subclass network.')
valid_types = (tuple, list, tensor_shape.TensorShape, dict)
if not isinstance(input_shape, valid_types):
    raise ValueError('Specified input shape is not one of the valid types. '
                     'Please specify a batch input shape of type tuple or '
                     'list of input shapes. User provided '
                     'input type: {}'.format(type(input_shape)))

if input_shape and not self.inputs:
    # We create placeholders for the `None`s in the shape and build the model
    # in a Graph. Since tf.Variable is compatible with both eager execution
    # and graph building, the variables created after building the model in
    # a Graph are still valid when executing eagerly.
    if context.executing_eagerly():
        graph = func_graph.FuncGraph('build_graph')
    else:
        graph = backend.get_graph()
    with graph.as_default():
        if (isinstance(input_shape, list) and
            all(d is None or isinstance(d, int) for d in input_shape)):
            input_shape = tuple(input_shape)
        if isinstance(input_shape, list):
            x = [base_layer_utils.generate_placeholders_from_shape(shape)
                 for shape in input_shape]
        elif isinstance(input_shape, dict):
            x = {
                k: base_layer_utils.generate_placeholders_from_shape(shape)
                for k, shape in input_shape.items()
            }
        else:
            x = base_layer_utils.generate_placeholders_from_shape(input_shape)

        kwargs = {}
        call_signature = self._call_full_argspec
        call_args = call_signature.args
        # Exclude `self`, `inputs`, and any argument with a default value.
        if len(call_args) > 2:
            if call_signature.defaults:
                call_args = call_args[2:-len(call_signature.defaults)]
            else:
                call_args = call_args[2:]
            for arg in call_args:
                if arg == 'training':
                    # Case where `training` is a positional arg with no default.
                    kwargs['training'] = False
                else:
                    # Has invalid call signature with unknown positional arguments.
                    raise ValueError(
                        'Currently, you cannot build your model if it has '
                        'positional or keyword arguments that are not '
                        'inputs to the model, but are required for its '
                        '`call` method. Instead, in order to instantiate '
                        'and build your model, `call` your model on real '
                        'tensor data with all expected call arguments.')
        elif len(call_args) < 2:
            # Signature without `inputs`.
            raise ValueError('You can only call `build` on a model if its `call` '
                             'method accepts an `inputs` argument.')
        try:
            self.call(x, **kwargs)
        except (errors.InvalidArgumentError, TypeError):
            raise ValueError('You cannot build your model by calling `build` '
                             'if your layers do not support float type inputs. '
                             'Instead, in order to instantiate and build your '
                             'model, `call` your model on real tensor data (of '
                             'the correct dtype).')
super(Model, self).build(input_shape)
