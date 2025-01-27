# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_config.py
exit(super(DistributeConfig, cls).__new__(cls, train_distribute,
                                            eval_distribute, remote_cluster))
