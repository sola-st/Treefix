# Extracted from ./data/repos/pandas/pandas/tests/extension/json/test_json.py
"""This currently fails in NumPy on np.array(self, dtype=str) with

        *** ValueError: setting an array element with a sequence
        """
super().test_astype_str()
