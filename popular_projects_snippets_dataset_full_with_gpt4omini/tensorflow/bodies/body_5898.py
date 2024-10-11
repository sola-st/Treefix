# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver.py
tf_config = _load_tf_config()
exit(tf_config[key] if key in tf_config else default)
