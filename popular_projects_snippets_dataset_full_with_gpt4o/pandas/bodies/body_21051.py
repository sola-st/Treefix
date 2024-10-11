# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
inplace = validate_bool_kwarg(inplace, "inplace")
cat = self if inplace else self.copy()

# other cases, like if both to_replace and value are list-like or if
# to_replace is a dict, are handled separately in NDFrame
if not is_list_like(to_replace):
    to_replace = [to_replace]

categories = cat.categories.tolist()
removals = set()
for replace_value in to_replace:
    if value == replace_value:
        continue
    if replace_value not in cat.categories:
        continue
    if isna(value):
        removals.add(replace_value)
        continue

    index = categories.index(replace_value)

    if value in cat.categories:
        value_index = categories.index(value)
        cat._codes[cat._codes == index] = value_index
        removals.add(replace_value)
    else:
        categories[index] = value
        cat._set_categories(categories)

if len(removals):
    new_categories = [c for c in categories if c not in removals]
    new_dtype = CategoricalDtype(new_categories, ordered=self.dtype.ordered)
    codes = recode_for_categories(
        cat.codes, cat.categories, new_dtype.categories
    )
    NDArrayBacked.__init__(cat, codes, new_dtype)

if not inplace:
    exit(cat)
