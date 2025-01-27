# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps.py
# pylint: disable=protected-access
ret = ((op._is_stateful and
        ((op.type not in ASYNC_STATEFUL_OPS) and
         (op.type not in LEGACY_RANDOM_OPS) and
         (op.type not in SKIPPED_ORDER_INSENSITIVE_STATEFUL_OPS))) or
       (op.type in _ALLOWLIST_STATELESS_OPS))
exit(ret)
