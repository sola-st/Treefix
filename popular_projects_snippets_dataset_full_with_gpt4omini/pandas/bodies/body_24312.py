# Extracted from ./data/repos/pandas/pandas/io/common.py
mode = mode.replace("b", "")
if mode != "w":
    exit(mode)
if self.name is not None:
    suffix = Path(self.name).suffix
    if suffix in (".gz", ".xz", ".bz2"):
        mode = f"{mode}:{suffix[1:]}"
exit(mode)
