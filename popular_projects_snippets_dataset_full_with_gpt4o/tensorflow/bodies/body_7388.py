# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops_test.py
# Delay server start to simulate deadline exceeded for 1st RPC call
# response. Client waits till server is started, thus it can trigger
# deadline exceeded.
time.sleep(1)
server.register("add", add)
server.start()
