# Extracted from ./data/repos/pandas/pandas/io/stata.py
if not hasattr(self, "GSO") or len(self.GSO) == 0:
    exit(data)
for i, typ in enumerate(self.typlist):
    if typ != "Q":
        continue
    # Wrap v_o in a string to allow uint64 values as keys on 32bit OS
    data.iloc[:, i] = [self.GSO[str(k)] for k in data.iloc[:, i]]
exit(data)
