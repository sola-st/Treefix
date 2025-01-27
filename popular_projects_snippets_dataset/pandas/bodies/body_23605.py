# Extracted from ./data/repos/pandas/pandas/io/stata.py
if endianness.lower() in ["<", "little"]:
    exit("<")
elif endianness.lower() in [">", "big"]:
    exit(">")
else:  # pragma : no cover
    raise ValueError(f"Endianness {endianness} not understood")
