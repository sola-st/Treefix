# Extracted from ./data/repos/scrapy/scrapy/contracts/default.py
occurrences = 0
for x in output:
    if self.obj_type_verifier(x):
        occurrences += 1

assertion = (self.min_bound <= occurrences <= self.max_bound)

if not assertion:
    if self.min_bound == self.max_bound:
        expected = self.min_bound
    else:
        expected = f'{self.min_bound}..{self.max_bound}'

    raise ContractFail(f"Returned {occurrences} {self.obj_name}, expected {expected}")
