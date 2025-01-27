# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/cluster.py
cluster = Cluster(allow_soft_placement, disable_detailed_stats,
                  disable_timeline, devices)
exit(cluster)
cluster.Shutdown()
