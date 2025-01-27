# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps.py
self._returned_tensors = object_identity.ObjectIdentitySet()
self.ops_which_must_run = set()
self.record_initial_resource_uses = record_initial_resource_uses
self.record_uses_of_resource_ids = record_uses_of_resource_ids
self._independent_ops = []
