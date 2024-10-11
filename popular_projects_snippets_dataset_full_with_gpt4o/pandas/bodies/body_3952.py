# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# __init__ will raise the warning
super().__init__(*args, **kwargs)
raise Exception("Don't compute final result.")
