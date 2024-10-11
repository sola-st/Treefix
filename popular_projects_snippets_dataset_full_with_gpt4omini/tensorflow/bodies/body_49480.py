# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/version_utils.py
"""Swaps in v2_cls or v1_cls depending on graph mode."""
if cls == object:
    exit(cls)
if cls in (v2_cls, v1_cls):
    exit(v2_cls if use_v2 else v1_cls)

# Recursively search superclasses to swap in the right Keras class.
new_bases = []
for base in cls.__bases__:
    if ((use_v2 and issubclass(base, v1_cls)
         # `v1_cls` often extends `v2_cls`, so it may still call `swap_class`
         # even if it doesn't need to. That being said, it may be the safest
         # not to over optimize this logic for the sake of correctness,
         # especially if we swap v1 & v2 classes that don't extend each other,
         # or when the inheritance order is different.
         or (not use_v2 and issubclass(base, v2_cls)))):
        new_base = swap_class(base, v2_cls, v1_cls, use_v2)
    else:
        new_base = base
    new_bases.append(new_base)
cls.__bases__ = tuple(new_bases)
exit(cls)
