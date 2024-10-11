# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/base.py
# For backwards compatibility, legacy layers do not use `ResourceVariable`
# by default.
self._use_resource_variables = False
scope = kwargs.pop('_scope', None)
self._reuse = kwargs.pop('_reuse', None)

# Avoid an incorrect lint error
self._trainable_weights = []
self.built = False

if dtype is None:
    # Indicates to infer dtype from inputs. When the V2 dtype behavior is
    # enabled, Keras layers default their dtype to floatx instead, so we pass
    # an "_infer" policy to keep the old V1 behavior.
    dtype = policy.Policy('_infer')

if 'autocast' not in kwargs:
    kwargs['autocast'] = False

# Mark that legacy layers should not be instrumented as Keras usage
self._disable_keras_instrumentation = True

super(Layer, self).__init__(trainable=trainable, name=name, dtype=dtype,
                            **kwargs)

if _is_in_keras_style_scope():
    if scope is not None:
        raise ValueError(
            'scope argument not allowed when keras style layers are enabled, '
            'but saw: {}'.format(scope))
    if self._reuse is not None:
        raise ValueError(
            'reuse argument not allowed when keras style layers are enabled, '
            'but saw: {}'.format(self._reuse))
    self._keras_style = True
else:
    self._keras_style = False

self._call_has_scope_arg = 'scope' in self._call_fn_args
if scope:
    with vs.variable_scope(scope) as captured_scope:
        self._scope = captured_scope
else:
    self._scope = None
self._current_scope = None
