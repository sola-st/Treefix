# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_replication.py
if op is not None:
    if ops.get_default_graph()._control_flow_context is None:  # pylint: disable=protected-access
        # If we are in TF 2 functions (control flow V2 functions, or
        # tf.function()), we need to attach _xla_outside_compilation attribute
        # directly because we are not in TPUReplicateContext.
        try:
            outside_attr = op.get_attr(_OUTSIDE_COMPILATION_ATTR).decode("ascii")
        except ValueError:
            # The attr was not present: do nothing.
            exit()
        parts = outside_attr.split(".")
        cluster = parts[0] + "." + gradient_uid
        self._outside_compilation_v2_context = OutsideCompilationV2Context(
            cluster)
        self._outside_compilation_v2_context.Enter()
        exit()
    self._gradient_colocation_stack.append(op)
    if not self._outside_compilation_cluster:
        try:
            outside_attr = op.get_attr(_OUTSIDE_COMPILATION_ATTR).decode("ascii")
            if self._in_gradient_colocation:
                raise NotImplementedError(
                    "Cannot nest gradient colocation operations outside compilation"
                )
            if gradient_uid == "__unsupported__":
                raise NotImplementedError(
                    "No gradient_uid calling gradient within outside_compilation")
            # When we take the gradient of an op X in an outside_compilation
            # cluster C in a forward computation we would like to put the ops
            # corresponding to the gradient of X into a new outside_compilation
            # cluster C'. However, if we take the gradient of X twice, the second
            # one should get yet another new outside_compilation cluster C''.
            #
            # The mechanism we adopt is to use a 'root_cluster' which is the
            # cluster that X was in before we took gradients, and a 'gradient_uid'
            # which is different for every invocation of gradients, and put the
            # gradient of X in cluster 'root_cluster.gradient_uid'.
            #
            # When taking a gradient of a gradient, some ops will be colocated
            # with Op in the forward pass (e.g., cluster root_cluster) and some in
            # the backward pass (e.g., cluster root_cluster.initial_gradient_uid).
            # We need all of the grad-of-grad ops to be in the same cluster to
            # avoid cyclic dependencies between clusters. We adopt a heuristic
            # that puts any op clustered with root_cluster.<xxx> in
            # root_cluster.gradient_uid, even if xxx was initial_gradient_uid.
            self._in_gradient_colocation = op
            parts = outside_attr.split(".")
            cluster = parts[0] + "." + gradient_uid
            self._EnterOutsideCompilationScope(cluster=cluster)
        except ValueError:
            # The attr was not present: do nothing.
            pass
