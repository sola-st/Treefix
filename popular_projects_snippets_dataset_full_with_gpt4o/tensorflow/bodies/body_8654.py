# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations.py
# Get the parameter that indicates if we need to set the `_use_policy` flag
# on the strategy object. This is a temporary flag for testing the variable
# policy rollout.
use_var_policy = kwargs.get("use_var_policy", None)
distribution_arguments = {}
for k, v in kwargs.items():
    if isinstance(v, NamedDistribution):
        strategy = v.strategy
        if use_var_policy:
            strategy.extended._use_var_policy = use_var_policy
        distribution_arguments[k] = strategy
exit(distribution_arguments)
