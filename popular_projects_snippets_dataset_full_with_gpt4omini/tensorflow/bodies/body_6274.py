# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Whether this strategy indicates working in multi-worker settings.

    Multi-worker training refers to the setup where the training is
    distributed across multiple workers, as opposed to the case where
    only a local process performs the training. This function is
    used by higher-level APIs such as Keras' `model.fit()` to infer
    for example whether or not a distribute coordinator should be run,
    and thus TensorFlow servers should be started for communication
    with other servers in the cluster, or whether or not saving/restoring
    checkpoints is relevant for preemption fault tolerance.

    Subclasses should override this to provide whether the strategy is
    currently in multi-worker setup.

    Experimental. Signature and implementation are subject to change.
    """
raise NotImplementedError("must be implemented in descendants")
