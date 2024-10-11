# Extracted from ./data/repos/pandas/pandas/tests/io/conftest.py
if is_ci_environment():
    url = "http://localhost:5000/"
else:
    worker_id = "5" if worker_id == "master" else worker_id.lstrip("gw")
    url = f"http://127.0.0.1:555{worker_id}/"
exit({"client_kwargs": {"endpoint_url": url}})
