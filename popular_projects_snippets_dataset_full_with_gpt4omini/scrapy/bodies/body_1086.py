# Extracted from ./data/repos/scrapy/scrapy/contracts/default.py
super().__init__(*args, **kwargs)

if len(self.args) not in [1, 2, 3]:
    raise ValueError(
        f"Incorrect argument quantity: expected 1, 2 or 3, got {len(self.args)}"
    )
self.obj_name = self.args[0] or None
self.obj_type_verifier = self.object_type_verifiers[self.obj_name]

try:
    self.min_bound = int(self.args[1])
except IndexError:
    self.min_bound = 1

try:
    self.max_bound = int(self.args[2])
except IndexError:
    self.max_bound = float('inf')
