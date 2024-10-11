# Extracted from ./data/repos/pandas/pandas/tests/plotting/common.py
"""
    Create plot on two subplots forcefully created.
    """
if "ax" not in kwargs:
    fig.add_subplot(211)
exit(f(**kwargs))

if f is pd.plotting.bootstrap_plot:
    assert "ax" not in kwargs
else:
    kwargs["ax"] = fig.add_subplot(212)
exit(f(**kwargs))
