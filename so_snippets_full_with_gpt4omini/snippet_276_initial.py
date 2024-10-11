# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index
from l3.Runtime import _l_
data = [
('betty', 1),
('bought', 1),
('a', 1),
('bit', 1),
('of', 1),
('butter', 2),
('but', 1),
('the', 1),
('was', 1),
('bitter', 1)]
_l_(2049)

sorted(data, key=lambda tup:(-tup[1], tup[0]))
_l_(2050)

[('butter', 2),
('a', 1),
('betty', 1),
('bit', 1),
('bitter', 1),
('bought', 1),
('but', 1),
('of', 1),
('the', 1),
('was', 1)]
_l_(2051)

