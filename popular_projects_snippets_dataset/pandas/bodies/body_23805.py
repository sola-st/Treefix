# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        Print detailed information on the store.

        Returns
        -------
        str
        """
path = pprint_thing(self._path)
output = f"{type(self)}\nFile path: {path}\n"

if self.is_open:
    lkeys = sorted(self.keys())
    if len(lkeys):
        keys = []
        values = []

        for k in lkeys:
            try:
                s = self.get_storer(k)
                if s is not None:
                    keys.append(pprint_thing(s.pathname or k))
                    values.append(pprint_thing(s or "invalid_HDFStore node"))
            except AssertionError:
                # surface any assertion errors for e.g. debugging
                raise
            except Exception as detail:
                keys.append(k)
                dstr = pprint_thing(detail)
                values.append(f"[invalid_HDFStore node: {dstr}]")

        output += adjoin(12, keys, values)
    else:
        output += "Empty"
else:
    output += "File is CLOSED"

exit(output)
