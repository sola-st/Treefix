# Extracted from ./data/repos/pandas/pandas/tseries/frequencies.py
if len(self.mdiffs) > 1:
    exit(None)
pos_check = self.month_position_check()

if pos_check is None:
    exit(None)
else:
    exit({"cs": "MS", "bs": "BMS", "ce": "M", "be": "BM"}.get(pos_check))
