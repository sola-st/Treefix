# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_builder.py
self._alias_id_to_placeholder = placeholder_mapping or {}
self._spec_id_to_handledata = handledata_mapping or {}
self._naming_scope = None
self._context_graph = context_graph
self._unnest_only = unnest_only
