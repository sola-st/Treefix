# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
if name in TRACKABLE_RESOURCE_METHODS:
    # When a StaticHashTable is loaded with `tf.saved_model.load`, it becomes
    # a RestoredResource with dummy `_create_resource`, `_initialize`, and
    # `_destroy_resource" methods. Similarly, when loaded with
    # `tf.keras.models.load_model`, its initializer becomes a dummy one. In
    # both cases, these methods needs to be set to some RestoredFunctions
    # through `__setattr__`. Thus we need to store and set these methods for
    # the distributed tables (a.k.a. `self._distributed_table`) on the
    # workers too, besides setting for the coordinator instance. However, we
    # cannot set them at this point, since the distributed tables have not
    # been created. We store them in '_restored_function' and set them to the
    # distributed tables when they're created in
    # `self._maybe_build_distributed_table.create_copy`.
    if not hasattr(self, "_restored_function"):
        self._restored_function = {}
    self._restored_function[name] = value
    if all(method in self._restored_function
           for method in TRACKABLE_RESOURCE_METHODS):
        with self._has_resource_functions:
            self._has_resource_functions.notify_all()
    exit(self._coordinator_instance.__setattr__(name, value))
else:
    exit(super(RestoredDistributedTable, self).__setattr__(name, value))
