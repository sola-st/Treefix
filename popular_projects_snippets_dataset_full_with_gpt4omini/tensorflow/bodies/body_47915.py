# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
if not created_variables and not accessed_variables:
    # In the common case that a Lambda layer does not touch a Variable, we
    # don't want to incur the runtime cost of assembling any state used for
    # checking only to immediately discard it.
    exit()

tracked_weights = set(v.ref() for v in self.weights)
untracked_new_vars = [
    v for v in created_variables if v.ref() not in tracked_weights
]
if untracked_new_vars:
    variable_str = '\n'.join('  {}'.format(i) for i in untracked_new_vars)
    error_str = textwrap.dedent(
        '''
          The following Variables were created within a Lambda layer ({name})
          but are not tracked by said layer:
          {variable_str}
          The layer cannot safely ensure proper Variable reuse across multiple
          calls, and consquently this behavior is disallowed for safety. Lambda
          layers are not well suited to stateful computation; instead, writing a
          subclassed Layer is the recommend way to define layers with
          Variables.'''
    ).format(name=self.name, variable_str=variable_str)
    raise ValueError(error_str)

untracked_used_vars = [
    v for v in accessed_variables if v.ref() not in tracked_weights
]
if untracked_used_vars and not self._already_warned:
    variable_str = '\n'.join('  {}'.format(i) for i in untracked_used_vars)
    self._warn(textwrap.dedent(
        '''
          The following Variables were used a Lambda layer's call ({name}), but
          are not present in its tracked objects:
          {variable_str}
          It is possible that this is intended behavior, but it is more likely
          an omission. This is a strong indication that this layer should be
          formulated as a subclassed Layer rather than a Lambda layer.'''
    ).format(name=self.name, variable_str=variable_str))
    self._already_warned = True
