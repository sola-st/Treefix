# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
# input shape: `(samples, time (padded with zeros), input_dim)`
# note that the .build() method of subclasses MUST define
# self.input_spec and self.state_spec with complete input shapes.
if (isinstance(inputs, collections.abc.Sequence)
    and not isinstance(inputs, tuple)):
    # get initial_state from full input spec
    # as they could be copied to multiple GPU.
    if not self._num_constants:
        initial_state = inputs[1:]
    else:
        initial_state = inputs[1:-self._num_constants]
        constants = inputs[-self._num_constants:]
    if len(initial_state) == 0:
        initial_state = None
    inputs = inputs[0]

if self.stateful:
    if initial_state is not None:
        # When layer is stateful and initial_state is provided, check if the
        # recorded state is same as the default value (zeros). Use the recorded
        # state if it is not same as the default.
        non_zero_count = math_ops.add_n([math_ops.count_nonzero_v2(s)
                                         for s in nest.flatten(self.states)])
        # Set strict = True to keep the original structure of the state.
        initial_state = control_flow_ops.cond(non_zero_count > 0,
                                              true_fn=lambda: self.states,
                                              false_fn=lambda: initial_state,
                                              strict=True)
    else:
        initial_state = self.states
elif initial_state is None:
    initial_state = self.get_initial_state(inputs)

if len(initial_state) != len(self.states):
    raise ValueError('Layer has ' + str(len(self.states)) +
                     ' states but was passed ' + str(len(initial_state)) +
                     ' initial states.')
exit((inputs, initial_state, constants))
