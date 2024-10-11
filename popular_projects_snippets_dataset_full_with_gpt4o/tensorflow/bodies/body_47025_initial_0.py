from typing import Any, Dict # pragma: no cover

class Policy:# pragma: no cover
    def __init__(self, name: str):# pragma: no cover
        self.name = name# pragma: no cover
    # pragma: no cover
    def get_config(self) -> Dict[str, Any]:# pragma: no cover
        return {'name': self.name} # pragma: no cover
policy = Policy('_infer') # pragma: no cover
def _is_convertible_to_dtype(name: str) -> bool:# pragma: no cover
    return name in ['float32', 'float64', 'int32', 'int64'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/policy.py
from l3.Runtime import _l_
"""Returns True if the Policy is equivalent to a single dtype.

  A policy is equivalent to a single dtype if the policy's compute and variable
  dtypes are the same and the policy's type is Policy and not a subclass of
  Policy (such as PolicyV1).

  The "_infer" policy is considered equivalent to a single dtype.

  Args:
    policy: A Policy.

  Returns:
    True, if the policy is equivalent to a single dtype.
  """
aux = (type(policy) == Policy and  # pylint: disable=unidiomatic-typecheck
        list(policy.get_config().keys()) == ['name'] and
        (policy.name == '_infer' or _is_convertible_to_dtype(policy.name)))
_l_(17978)
# We use type() instead of isinstance because a subclass of Policy is never
# equivalent to a dtype.
exit(aux)
