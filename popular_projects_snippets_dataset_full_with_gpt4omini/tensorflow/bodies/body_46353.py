# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
name = anno.getanno(node, anno.Basic.QN)

if isinstance(node.ctx, gast.Load):
    types = self.types_in.types.get(name, None)
    if types is None:
        if (name not in self.scope.bound) or (name in self.scope.nonlocals):
            # TODO(mdan): Test with global variables.
            if name in self.closure_types:
                types = self.closure_types[name]
            else:
                types, value = self.resolver.res_name(
                    self.namespace, self.types_in.types, name)
                if value is not None:
                    anno.setanno(node, anno.Static.VALUE, value)

elif isinstance(node.ctx, gast.Param):
    # The direct parent it the whole function scope. See activity.py.
    f_is_local = self.scope.parent.parent is not None

    type_name = anno.getanno(node.annotation, anno.Basic.QN, None)
    types = self.resolver.res_arg(self.namespace, self.types_in.types,
                                  self.scope.function_name, name, type_name,
                                  f_is_local)
    if types is not None:
        self.new_symbols[name] = types

elif isinstance(node.ctx, gast.Store):
    if self.rtype is not None:
        self.new_symbols[name] = self.rtype
    types = self.rtype

else:
    assert False, 'unknown ctx'

if __debug__:
    self._check_set(types)

exit(types)
