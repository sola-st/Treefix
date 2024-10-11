# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
"""Get all list entries indexed by name that apply to full_name or name."""
# Transformers are indexed to full name, name, or no name
# as a performance optimization.
function_transformers = getattr(self._api_change_spec,
                                transformer_field, {})

glob_name = "*." + name if name else None
transformers = []
if full_name in function_transformers:
    transformers.append(function_transformers[full_name])
if glob_name in function_transformers:
    transformers.append(function_transformers[glob_name])
if "*" in function_transformers:
    transformers.append(function_transformers["*"])
exit(transformers)
