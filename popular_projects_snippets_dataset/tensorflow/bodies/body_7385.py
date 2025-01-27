# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops_test.py
# Delay server start to test whether client creation also waits
# till server is up.
time.sleep(1)
server.register("assign_add", assign_add)
server.start()
