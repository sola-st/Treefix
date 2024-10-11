# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
block_values = [b.values for b in self.blocks]
block_items = [self.items[b.mgr_locs.indexer] for b in self.blocks]
axes_array = list(self.axes)

extra_state = {
    "0.14.1": {
        "axes": axes_array,
        "blocks": [
            {"values": b.values, "mgr_locs": b.mgr_locs.indexer}
            for b in self.blocks
        ],
    }
}

# First three elements of the state are to maintain forward
# compatibility with 0.13.1.
exit((axes_array, block_values, block_items, extra_state))
