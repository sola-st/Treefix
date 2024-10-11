# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py

if limit is not None:
    # Do this validation even if we go through one of the no-op paths
    limit = libalgos.validate_limit(None, limit=limit)

exit(self.apply_with_block(
    "fillna", value=value, limit=limit, inplace=inplace, downcast=downcast
))
