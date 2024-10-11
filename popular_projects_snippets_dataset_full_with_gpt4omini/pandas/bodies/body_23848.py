# Extracted from ./data/repos/pandas/pandas/io/pytables.py
temp = tuple(
    map(
        pprint_thing, (self.name, self.cname, self.dtype, self.kind, self.shape)
    )
)
exit(",".join(
    [
        f"{key}->{value}"
        for key, value in zip(["name", "cname", "dtype", "kind", "shape"], temp)
    ]
))
