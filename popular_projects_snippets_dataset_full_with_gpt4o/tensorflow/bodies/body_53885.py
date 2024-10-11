# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""See session() for details."""

def prepare_config(config):
    """Returns a config for sessions.

      Args:
        config: An optional config_pb2.ConfigProto to use to configure the
          session.

      Returns:
        A config_pb2.ConfigProto object.
      """
    # TODO(b/114333779): Enforce allow_soft_placement=False when
    # use_gpu=False. Currently many tests rely on the fact that any device
    # will be used even when a specific device is supposed to be used.
    allow_soft_placement = not force_gpu
    if config is None:
        config = context.context().config
        config.allow_soft_placement = allow_soft_placement
    elif not allow_soft_placement and config.allow_soft_placement:
        config_copy = context.context().config
        config = config_copy
        config.allow_soft_placement = False
    # Don't perform optimizations for tests so we don't inadvertently run
    # gpu ops on cpu
    config.graph_options.optimizer_options.opt_level = -1
    # Disable Grappler constant folding since some tests & benchmarks
    # use constant input and become meaningless after constant folding.
    # DO NOT DISABLE GRAPPLER OPTIMIZERS WITHOUT CONSULTING WITH THE
    # GRAPPLER TEAM.
    config.graph_options.rewrite_options.constant_folding = (
        rewriter_config_pb2.RewriterConfig.OFF)
    config.graph_options.rewrite_options.pin_to_host_optimization = (
        rewriter_config_pb2.RewriterConfig.OFF)
    exit(config)

exit(ErrorLoggingSession(graph=graph, config=prepare_config(config)))
