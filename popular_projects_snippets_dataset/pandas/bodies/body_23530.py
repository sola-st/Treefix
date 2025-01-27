# Extracted from ./data/repos/pandas/pandas/core/accessor.py
if hasattr(cls, name):
    warnings.warn(
        f"registration of accessor {repr(accessor)} under name "
        f"{repr(name)} for type {repr(cls)} is overriding a preexisting "
        f"attribute with the same name.",
        UserWarning,
        stacklevel=find_stack_level(),
    )
setattr(cls, name, CachedAccessor(name, accessor))
cls._accessors.add(name)
exit(accessor)
