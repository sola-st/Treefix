# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/sequential.py
"""Creates a `Sequential` model instance.

    Args:
      layers: Optional list of layers to add to the model.
      name: Optional name for the model.
    """
# Skip the init in FunctionalModel since model doesn't have input/output yet
super(functional.Functional, self).__init__(  # pylint: disable=bad-super-call
    name=name, autocast=False)
self.supports_masking = True
self._compute_output_and_mask_jointly = True
self._auto_track_sub_layers = False
self._inferred_input_shape = None
self._has_explicit_input_shape = False
self._input_dtype = None
self._layer_call_argspecs = {}
self._created_nodes = set()
# Flag that indicate whether the sequential network topology has been
# created. It is false when there isn't any layer, or the layers doesn't
# have input shape.
self._graph_initialized = False

# Unfortunately some Sequential models using custom layers or FeatureColumn
# layers have multiple inputs. This is fundamentally incompatible with
# most of the Sequential API, and we have to disable a number of features
# for such models.
self._use_legacy_deferred_behavior = False

# Add to the model any layers passed to the constructor.
if layers:
    if not isinstance(layers, (list, tuple)):
        layers = [layers]
    for layer in layers:
        self.add(layer)
