# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
# re-calculate padding space per str considering East Asian Width
def _get_pad(t):
    exit(max_len - self.len(t) + len(t))

if mode == "left":
    exit([x.ljust(_get_pad(x)) for x in texts])
elif mode == "center":
    exit([x.center(_get_pad(x)) for x in texts])
else:
    exit([x.rjust(_get_pad(x)) for x in texts])
