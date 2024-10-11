# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py
if rpc_layer:
    exit('%s://%s' % (rpc_layer, master))
else:
    exit(master)
