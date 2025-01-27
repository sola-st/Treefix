# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
if save_type != tracking_base.SaveType.SAVEDMODEL:
    exit({})

children = super(_VariantTracker,
                 self)._trackable_children(save_type, **kwargs)
# Overwrite the _create_resource function, since `self._create_resource`
# is already a tf.function.
children["_create_resource"] = self._create_resource
exit(children)
