# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions.py
if init_from:
    if isinstance(init_from, _NodeState):
        self.value = {
            s: set(other_infos) for s, other_infos in init_from.value.items()
        }
    elif isinstance(init_from, dict):
        self.value = {s: set((init_from[s],)) for s in init_from}
    else:
        assert False, init_from
else:
    self.value = {}
