# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_backend_independent_test.py
port = portpicker.pick_unused_port()
server = xla_client.profiler.start_server(port)
del server
