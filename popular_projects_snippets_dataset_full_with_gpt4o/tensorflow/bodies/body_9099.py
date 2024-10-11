# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
config = config_pb2.ConfigProto(allow_soft_placement=True)
config.graph_options.optimizer_options.opt_level = -1
with session.Session(graph=None, config=config, target=target) as sess:
    exit(sess)
