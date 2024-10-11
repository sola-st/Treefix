# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_util.py
"""Creates a CollectiveHints.

    Args:
      bytes_per_pack: a non-negative integer. Breaks collective operations into
        packs of certain size. If it's zero, the value is determined
        automatically. This hint is respected by all multi-replica strategies
        except `TPUStrategy`.
      timeout_seconds: a float or None, timeout in seconds. If not None, the
        collective raises `tf.errors.DeadlineExceededError` if it takes longer
        than this timeout. Zero disables timeout. This can be useful when
        debugging hanging issues.  This should only be used for debugging since
        it creates a new thread for each collective, i.e. an overhead of
        `timeout_seconds * num_collectives_per_second` more threads. This only
        works for `tf.distribute.experimental.MultiWorkerMirroredStrategy`.
      implementation: a
        `tf.distribute.experimental.CommunicationImplementation`. This is a hint
        on the preferred communication implementation. Possible values include
        `AUTO`, `RING`, and `NCCL`. NCCL is generally more performant for GPU,
        but doesn't work for CPU. This only works for
        `tf.distribute.experimental.MultiWorkerMirroredStrategy`.

    Raises:
      ValueError: When arguments have invalid value.
    """
pass
