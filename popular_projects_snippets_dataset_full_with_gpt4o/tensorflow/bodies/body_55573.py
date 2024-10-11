# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
"""Ensures all inputs passed into _apply_op_helper were used."""
if keywords:
    all_keywords = ", ".join(sorted(keywords.keys()))
    raise TypeError(f"{op_type_name} got unexpected keyword arguments: "
                    f"{all_keywords}.")
