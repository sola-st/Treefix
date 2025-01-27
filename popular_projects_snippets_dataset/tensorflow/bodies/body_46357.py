# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
self.visit(node.func)

f_name = anno.Basic.QN.of(node.func)
arg_types = [self.visit(a) for a in node.args]
keyword_types = [self.visit(kw.value) for kw in node.keywords]

if f_name in self.scope.bound:
    # Local function, use local type definitions, if available.
    f_type = self.types_in.types.get(f_name, None)
    if f_type is None:
        # No static type info available, nothing more to do.
        ret_type, side_effects = None, None
    else:
        ret_type, side_effects = self._resolve_typed_callable(
            f_type, arg_types, keyword_types)

else:
    # Nonlocal function, resolve externally.
    f_type = anno.Static.TYPES.of(node.func, None)
    ret_type, side_effects = self.resolver.res_call(self.namespace,
                                                    self.types_in.types, node,
                                                    f_type, arg_types,
                                                    keyword_types)

if __debug__:
    self._check_set(ret_type)
    if side_effects:
        if not isinstance(side_effects, dict):
            raise ValueError(
                'side effects must be dict, got {}'.format(side_effects))
        for k, v in side_effects.items():
            if not isinstance(k, qual_names.QN):
                raise ValueError('side effect keys must be QNs, got {}'.format(k))
            self._check_set(v)

if side_effects:
    self.new_symbols.update(side_effects)
exit(ret_type)
