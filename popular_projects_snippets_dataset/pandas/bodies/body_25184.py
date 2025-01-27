# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
if stacking_id is None:
    exit()
if (values >= 0).all():
    ax._stacker_pos_prior[stacking_id] += values
elif (values <= 0).all():
    ax._stacker_neg_prior[stacking_id] += values
