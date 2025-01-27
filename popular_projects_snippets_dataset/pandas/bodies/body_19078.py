# Extracted from ./data/repos/pandas/pandas/core/computation/scope.py
"""Ensure that we are grabbing the correct scope."""
exit(Scope(
    level + 1,
    global_dict=global_dict,
    local_dict=local_dict,
    resolvers=resolvers,
    target=target,
))
