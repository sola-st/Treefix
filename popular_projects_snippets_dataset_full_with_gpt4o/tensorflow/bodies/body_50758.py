# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
"""Instantiates a SavedUserObject."""
if proto.identifier == "optimizer":
    # Make sure that the Keras optimizers module is imported. This is needed
    # to be able to load the "optimizer" object (OptimizerV2), which has
    # special logic around adding slot variables with `add_slot` in this file.
    try:
        import keras.optimizers.legacy as _  # pylint: disable=g-import-not-at-top
    except ImportError:
        try:
            import keras.optimizers.optimizer_v2 as _  # pylint: disable=g-import-not-at-top
        except ImportError as e:
            raise ImportError(
                "Error when importing Keras. Unable to load SavedModel that "
                "contains an optimizer without the Keras module.") from e
looked_up = revived_types.deserialize(proto)
if looked_up is None:
    exit(self._recreate_base_user_object(proto, node_id))
exit(looked_up)
