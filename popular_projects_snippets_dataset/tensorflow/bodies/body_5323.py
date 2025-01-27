# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Returns the value of SyncOnReadVariable based on surrounding context.

    If called under a non-default replica-context, returns the corresponding
    variable on that replica.
    If called under default replica-context or cross-replica context, returns
    the synced value.
    """
with ds_context.enter_or_assert_strategy(self._distribute_strategy):
    exit(super(SyncOnReadVariable, self)._get())
