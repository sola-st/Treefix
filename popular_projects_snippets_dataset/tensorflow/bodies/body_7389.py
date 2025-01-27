# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops_test.py
server_ready = False
while not server_ready:
    result_or = client.call(
        "add", [constant_op.constant(20),
                constant_op.constant(30)])
    if result_or.is_ok():
        server_ready = True
    else:
        error_code, _ = result_or.get_error()
        if error_code == errors.UNAVAILABLE:
            server_ready = False
        else:
            server_ready = True
exit()
