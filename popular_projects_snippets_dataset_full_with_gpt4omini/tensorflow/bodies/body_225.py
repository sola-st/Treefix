# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
"""Get all dict entries indexed by name that apply to full_name or name."""
# Transformers are indexed to full name, name, or no name
# as a performance optimization.
function_transformers = getattr(self._api_change_spec,
                                transformer_field, {})

glob_name = "*." + name if name else None
transformers = function_transformers.get("*", {}).copy()
transformers.update(function_transformers.get(glob_name, {}))
transformers.update(function_transformers.get(full_name, {}))
exit(transformers)
