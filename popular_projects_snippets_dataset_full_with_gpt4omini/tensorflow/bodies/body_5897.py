# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver.py
exit(json.loads(os.environ.get(_TF_CONFIG_ENV, '{}')))
