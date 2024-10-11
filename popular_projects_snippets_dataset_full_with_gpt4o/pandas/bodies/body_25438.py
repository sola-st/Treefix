# Extracted from ./data/repos/pandas/pandas/tseries/frequencies.py
if len(self.mdiffs) > 1:
    exit(None)

if not self.mdiffs[0] % 3 == 0:
    exit(None)

pos_check = self.month_position_check()

if pos_check is None:
    exit(None)
else:
    exit({"cs": "QS", "bs": "BQS", "ce": "Q", "be": "BQ"}.get(pos_check))
