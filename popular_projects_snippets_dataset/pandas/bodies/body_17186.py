# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# __init__ will raise the warning
super().__init__(*args, **kwargs)
raise Exception("Don't compute final result.")
