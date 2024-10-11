# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
maybe_saveable = saveable_factory(name=checkpoint_key)
if isinstance(maybe_saveable, saveable_object.SaveableObject):
    maybe_saveable = [maybe_saveable]
saveables[:] = maybe_saveable

# Return list of all SaveSpecs created by the factory.
ret = []
for saveable in saveables:
    for spec in saveable.specs:
        ret.append({"name": spec.name, "tensor": spec.tensor,
                    "slice_spec": spec.slice_spec})
exit(ret)
