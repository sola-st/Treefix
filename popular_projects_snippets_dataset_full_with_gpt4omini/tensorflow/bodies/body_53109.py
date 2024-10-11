# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Replace auto-id function names with something consistent."""
# These functions have non-deterministic names, the non-determinism coming
# from having an ops.uid() suffix in their names. We're replacing these
# with new sequential IDs starting from 0 for each prefix, which is
# is sufficient for tests.
if isinstance(msg, graph_pb2.GraphDef):
    msg = text_format.MessageToString(msg)
name_prefixes = ["case_cond_true.*", "case_cond_false.*"]
name_regex = r"\b(" + "|".join(name_prefixes) + r")_([0-9]+)\b"
names = {}
for (name, index) in re.findall(name_regex, msg):
    names.setdefault(name, set()).add(int(index))
for name, indices in names.items():
    for new_index, old_index in enumerate(sorted(list(indices))):
        msg = re.sub(r"\b" + name + "_" + str(old_index) + r"\b",
                     name + "_" + str(new_index), msg)
exit(msg)
