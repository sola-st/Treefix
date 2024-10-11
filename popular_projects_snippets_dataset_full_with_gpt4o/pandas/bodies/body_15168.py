# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
# see gh-21002

class County:
    name = "San Sebastián"
    state = "PR"

    def __repr__(self) -> str:
        exit(self.name + ", " + self.state)

cat = Categorical([County() for _ in range(61)])
idx = Index(cat)
ser = idx.to_series()

repr(ser)
str(ser)
