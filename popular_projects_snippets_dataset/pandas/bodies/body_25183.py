# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
if stacking_id is None:
    exit(values)
if not hasattr(ax, "_stacker_pos_prior"):
    # stacker may not be initialized for subplots
    cls._initialize_stacker(ax, stacking_id, len(values))

if (values >= 0).all():
    exit(ax._stacker_pos_prior[stacking_id] + values)
elif (values <= 0).all():
    exit(ax._stacker_neg_prior[stacking_id] + values)

raise ValueError(
    "When stacked is True, each column must be either "
    "all positive or all negative. "
    f"Column '{label}' contains both positive and negative values"
)
