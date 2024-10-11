# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
updates = updates or []
if not isinstance(updates, (list, tuple)):
    raise TypeError('`updates` in a Keras backend function '
                    'should be a list or tuple.')

self._inputs_structure = inputs
self.inputs = nest.flatten(inputs, expand_composites=True)
self._outputs_structure = outputs
self.outputs = cast_variables_to_tensor(
    nest.flatten(outputs, expand_composites=True))
# TODO(b/127668432): Consider using autograph to generate these
# dependencies in call.
# Index 0 = total loss or model output for `predict`.
with ops.control_dependencies([self.outputs[0]]):
    updates_ops = []
    for update in updates:
        if isinstance(update, tuple):
            p, new_p = update
            updates_ops.append(state_ops.assign(p, new_p))
        else:
            # assumed already an op
            updates_ops.append(update)
    self.updates_op = control_flow_ops.group(*updates_ops)
self.name = name
# additional tensor substitutions
self.feed_dict = session_kwargs.pop('feed_dict', None)
# additional operations
self.fetches = session_kwargs.pop('fetches', [])
if not isinstance(self.fetches, list):
    self.fetches = [self.fetches]
self.run_options = session_kwargs.pop('options', None)
self.run_metadata = session_kwargs.pop('run_metadata', None)
# The main use case of `fetches` being passed to a model is the ability
# to run custom updates
# This requires us to wrap fetches in `identity` ops.
self.fetches = [array_ops.identity(x) for x in self.fetches]
self.session_kwargs = session_kwargs
# This mapping keeps track of the function that should receive the
# output from a fetch in `fetches`: { fetch: function(fetch_output) }
# A Callback can use this to register a function with access to the
# output values for a fetch it added.
self.fetch_callbacks = {}

if session_kwargs:
    raise ValueError('Some keys in session_kwargs are not supported at this '
                     'time: %s' % (session_kwargs.keys(),))

self._callable_fn = None
self._feed_arrays = None
self._feed_symbols = None
self._symbol_vals = None
self._fetches = None
self._session = None
