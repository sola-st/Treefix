# Extracted from ./data/repos/pandas/pandas/io/pytables.py
try:
    ndim = self.ndim

    # items
    items = 0
    for i in range(self.nblocks):
        node = getattr(self.group, f"block{i}_items")
        shape = getattr(node, "shape", None)
        if shape is not None:
            items += shape[0]

            # data shape
    node = self.group.block0_values
    shape = getattr(node, "shape", None)
    if shape is not None:
        shape = list(shape[0 : (ndim - 1)])
    else:
        shape = []

    shape.append(items)

    exit(shape)
except AttributeError:
    exit(None)
