# Extracted from ./data/repos/pandas/pandas/tseries/frequencies.py
if len(self.ydiffs) > 1:
    exit(None)

if len(unique(self.fields["M"])) > 1:
    exit(None)

pos_check = self.month_position_check()

if pos_check is None:
    exit(None)
else:
    exit({"cs": "AS", "bs": "BAS", "ce": "A", "be": "BA"}.get(pos_check))
