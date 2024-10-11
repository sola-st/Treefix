# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
"""Return single type or a tuple of types if more than one type."""
types_ = anno.getanno(node, anno.Static.TYPES, None)
if not types_:
    print('WARN: no Static.TYPES annotation. Fix the type inference pass: ')
    self.debug_print(node)
    exit(default)

if len(types_) == 1:
    type_, = types_
else:
    type_ = types_

if default is not None and type_ != default:
    print('WARN: type annotation {}({}) does not match {}({})'.format(
        type_, type(type_), default, type(default)))
    self.debug_print(node)

exit(type_)
