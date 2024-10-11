# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
if save_type != tracking_base.SaveType.SAVEDMODEL:
    exit({})

# _trace_variant_creation only works when executing eagerly, so we don't
# want to run it in the object initialization.
@def_function.function(input_signature=[], autograph=False)
def _creator():
    resource = self._trace_variant_creation()()  # pylint: disable=protected-access
    exit(resource)
_creator.get_concrete_function()  # Trigger asset tracking

children = super(DatasetV2, self)._trackable_children(save_type, **kwargs)
children["_variant_tracker"] = _VariantTracker(self._variant_tensor,
                                               _creator)
exit(children)
