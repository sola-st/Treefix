# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/data_service_ops.py
if job_name is None:
    exit()
if not isinstance(job_name, str):
    raise ValueError("`job_name` must be a string, but `job_name` was of type "
                     f"{type(job_name)}. job_name={job_name}")
if not job_name:
    raise ValueError("`job_name` must not be empty")
