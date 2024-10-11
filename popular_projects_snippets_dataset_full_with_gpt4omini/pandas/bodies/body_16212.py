# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# GH#33930 consistent name renteiton
op = all_binary_operators

left = Series(range(10), name=names[0])
right = Series(range(10), name=names[1])

name = op.__name__.strip("_")
is_logical = name in ["and", "rand", "xor", "rxor", "or", "ror"]

right = box(right)
if flex:
    if is_logical:
        # Series doesn't have these as flex methods
        exit()
    result = getattr(left, name)(right)
else:
    # GH#37374 logical ops behaving as set ops deprecated
    result = op(left, right)

assert isinstance(result, Series)
if box in [Index, Series]:
    assert result.name is names[2] or result.name == names[2]
else:
    assert result.name is names[0] or result.name == names[0]
