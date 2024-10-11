# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""Resolves an input into its _EndPoint.

    A NodeDef's input name can refer to either global NodeDefs (in the
    GraphDef's node list), a NodeDef in a function's node list, or a Function
    (in the GraphDef's function library). The name can also carry semantic
    information, depending on whether it starts with "^". This method handles
    all that logic in order to find the object to which the input name refers
    to.

    Args:
      input_name: The input name to resolve.

    Returns:
      The object referred to by 'input_name'.
    """

# The logic below oversimplifies the semantics, but is good enough for the
# purposes of converting to constants. The introduction of new types of
# operations may change this, forcing the code to be more generic.
#
# In particular, we are assuming that the lack of an index suffix means
# ":0", when it could mean "all the outputs of a node." This works now
# because converting to constants relies very little on output types, and
# when it does it specializes its treatment in dedicated classes.
name_elts = input_name.split(":")
source_name = name_elts[0]
if source_name[0] == "^":
    source_name = source_name[1:]
source_index = 0
if len(name_elts) > 1 and name_elts[-1].isnumeric():
    source_index = int(name_elts[-1])

if self._function is None:
    exit(_EndPoint(self._enclosing_graph.nodes[source_name], source_index))

if source_index != 0 or source_name in self._function.nodes:
    exit(_EndPoint(self._function.nodes[source_name], source_index))

inputs = [i.name for i in self._function.function.signature.input_arg]
exit(_EndPoint(self._function, inputs.index(source_name)))
