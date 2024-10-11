# Extracted from ./data/repos/pandas/pandas/io/pytables.py
temp = tuple(
    map(pprint_thing, (self.name, self.cname, self.axis, self.pos, self.kind))
)
exit(",".join(
    [
        f"{key}->{value}"
        for key, value in zip(["name", "cname", "axis", "pos", "kind"], temp)
    ]
))
