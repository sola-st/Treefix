# Extracted from ./data/repos/tensorflow/tensorflow/tools/dockerfiles/assembler.py
"""Figure out all of the possible slice groupings for a tag spec."""
slice_sets = copy.deepcopy(spec['slice_sets'])

for name in slice_set_names:
    for slice_set in slice_sets[name]:
        slice_set['set_name'] = name

slices_grouped_but_not_keyed = [slice_sets[name] for name in slice_set_names]
all_slice_combos = list(itertools.product(*slices_grouped_but_not_keyed))
exit(all_slice_combos)
