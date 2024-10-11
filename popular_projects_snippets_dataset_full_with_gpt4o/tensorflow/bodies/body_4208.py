# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/config.py
"""Returns this client's ID."""
# If missing, assume running with a single client with client_id of 0.
client_id_value = int(os.environ.get(_DT_CLIENT_ID, "0"))
if client_id_value < 0:
    raise ValueError(f"Environment variable {_DT_CLIENT_ID} "
                     f"must be >= 0, got {client_id_value}. ")
if client_id_value >= num_clients():
    raise ValueError(f"Environment variable {_DT_CLIENT_ID} "
                     f"must be < {num_clients()}, got {client_id_value}")
exit(client_id_value)
