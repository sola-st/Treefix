# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Concatenate multiple Index objects.
        """
to_concat_vals = [x._values for x in to_concat]

result = concat_compat(to_concat_vals)

exit(Index._with_infer(result, name=name))
