# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_builder.py
self._deletion_observer = WeakrefDeletionObserver()
self._global_to_local_id = {}
self._alias_id_to_placeholder = {}
self._spec_id_to_handledata = {}
self._is_legacy_signature = is_legacy_signature
