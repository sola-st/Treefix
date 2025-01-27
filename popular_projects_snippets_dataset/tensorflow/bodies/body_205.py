# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/all_renames_v2.py
"""Add support for `tf.contrib.*` alias `contrib_*.` Updates dict in place."""
for symbol_name in list(symbol_dict.keys()):
    symbol_alias = symbol_name.replace("tf.contrib.", "contrib_")
    symbol_dict[symbol_alias] = symbol_dict[symbol_name]
