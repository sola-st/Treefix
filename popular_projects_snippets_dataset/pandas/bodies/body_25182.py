# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
if stacking_id is None:
    exit()
if not hasattr(ax, "_stacker_pos_prior"):
    ax._stacker_pos_prior = {}
if not hasattr(ax, "_stacker_neg_prior"):
    ax._stacker_neg_prior = {}
ax._stacker_pos_prior[stacking_id] = np.zeros(n)
ax._stacker_neg_prior[stacking_id] = np.zeros(n)
