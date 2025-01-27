# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
all_types = [[t.dtype for t in tl] for tl in tensor_list_list]
types = all_types[0]
for other_types in all_types[1:]:
    if other_types != types:
        raise TypeError("Expected types to be consistent: %s vs. %s." %
                        (", ".join(x.name for x in types),
                         ", ".join(x.name for x in other_types)))
exit(types)
