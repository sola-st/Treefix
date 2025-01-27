# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
inputs, initial_state, constants = _standardize_args(inputs,
                                                     initial_state,
                                                     constants,
                                                     self._num_constants)

if initial_state is None and constants is None:
    exit(super(RNN, self).__call__(inputs, **kwargs))

# If any of `initial_state` or `constants` are specified and are Keras
# tensors, then add them to the inputs and temporarily modify the
# input_spec to include them.

additional_inputs = []
additional_specs = []
if initial_state is not None:
    additional_inputs += initial_state
    self.state_spec = nest.map_structure(
        lambda s: InputSpec(shape=backend.int_shape(s)), initial_state)
    additional_specs += self.state_spec
if constants is not None:
    additional_inputs += constants
    self.constants_spec = [
        InputSpec(shape=backend.int_shape(constant)) for constant in constants
    ]
    self._num_constants = len(constants)
    additional_specs += self.constants_spec
# additional_inputs can be empty if initial_state or constants are provided
# but empty (e.g. the cell is stateless).
flat_additional_inputs = nest.flatten(additional_inputs)
is_keras_tensor = backend.is_keras_tensor(
    flat_additional_inputs[0]) if flat_additional_inputs else True
for tensor in flat_additional_inputs:
    if backend.is_keras_tensor(tensor) != is_keras_tensor:
        raise ValueError('The initial state or constants of an RNN'
                         ' layer cannot be specified with a mix of'
                         ' Keras tensors and non-Keras tensors'
                         ' (a "Keras tensor" is a tensor that was'
                         ' returned by a Keras layer, or by `Input`)')

if is_keras_tensor:
    # Compute the full input spec, including state and constants
    full_input = [inputs] + additional_inputs
    if self.built:
        # Keep the input_spec since it has been populated in build() method.
        full_input_spec = self.input_spec + additional_specs
    else:
        # The original input_spec is None since there could be a nested tensor
        # input. Update the input_spec to match the inputs.
        full_input_spec = generic_utils.to_list(
            nest.map_structure(lambda _: None, inputs)) + additional_specs
    # Perform the call with temporarily replaced input_spec
    self.input_spec = full_input_spec
    output = super(RNN, self).__call__(full_input, **kwargs)
    # Remove the additional_specs from input spec and keep the rest. It is
    # important to keep since the input spec was populated by build(), and
    # will be reused in the stateful=True.
    self.input_spec = self.input_spec[:-len(additional_specs)]
    exit(output)
else:
    if initial_state is not None:
        kwargs['initial_state'] = initial_state
    if constants is not None:
        kwargs['constants'] = constants
    exit(super(RNN, self).__call__(inputs, **kwargs))
