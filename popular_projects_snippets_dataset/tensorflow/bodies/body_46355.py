# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
f_name = qual_names.QN(node.name)

if node.decorator_list:
    raise NotImplementedError('decorators: {}'.format(node.decorator_list))

ret_types = None
if node.returns:
    ret_types, _ = self.resolver.res_name(
        self.namespace, self.types_in.types, anno.Basic.QN.of(node.returns))
    if __debug__:
        self._check_set(ret_types)

if ret_types is None:
    ret_types = {Any}

f_types = set()
for rt in ret_types:
    f_types.add(Callable[[Any], rt])

self.new_symbols[f_name] = f_types
# The definition of a function is an expression, hence has no return value.
exit(None)
