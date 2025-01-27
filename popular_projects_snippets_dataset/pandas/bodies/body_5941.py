# Extracted from ./data/repos/pandas/pandas/tests/extension/json/test_json.py
"""
        This fails in Index._do_unique_check with

        >   hash(val)
        E   TypeError: unhashable type: 'UserDict' with

        I suspect that once we support Index[ExtensionArray],
        we'll be able to dispatch unique.
        """
super().test_groupby_extension_apply()
