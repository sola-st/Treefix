# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_deprecated_py2.py
modified_live = scope.modified & node_defined_in
# Composite symbols are handled elsewhere see _create_state_functions
exit({s for s in modified_live if not s.is_composite()})
