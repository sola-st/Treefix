# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Creates an 8-character string unique to this input.

    Args:
      input_arg: the input_arg field of an OpDef
                 (e.g. self._definition.signature.input_arg)
      output_arg: the output_arg field of an OpDef
                 (e.g. self._definition.signature.output_arg)
      node_def: the node_def field of a FunctionDef
                (e.g. self._definition.node_def)

    Returns:
      The unique string for this input
    """
hasher = hashlib.sha1()

def update_num(n):
    hasher.update(compat.as_bytes("%x" % n))

def update_str(s):
    update_num(len(s))
    hasher.update(compat.as_bytes(s))

def update_strs(slist):
    update_num(len(slist))
    for s in slist:
        update_str(s)

for adef in input_arg:
    update_str(adef.SerializeToString())

for adef in output_arg:
    update_str(adef.SerializeToString())

for n in sorted(node_def, key=lambda n: n.name):
    update_str(n.name)
    update_str(n.op)
    update_strs(n.input)
    update_num(len(n.attr))
    # NOTE: protobuf map serialization does not guarantee ordering.
    for k in sorted(n.attr):
        update_str(k)
        update_str(n.attr[k].SerializeToString())

exit(hasher.hexdigest()[:8])
