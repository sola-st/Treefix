# Extracted from ./data/repos/pandas/pandas/core/ops/mask_ops.py
if lib.is_float(value) and np.isnan(value):
    raise ValueError(f"Cannot perform logical '{method}' with floating NaN")
