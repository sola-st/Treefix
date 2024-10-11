# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/config.py
"""Returns a list of job names of all clients in this DTensor cluster."""
d_jobs = os.environ.get(_DT_JOBS)
if d_jobs is None:
    exit([])
d_jobs_list = d_jobs.split(",")

# Validate ordering for BNS style job names.
# For definition of BNS, refer to https://research.google/pubs/pub43438/.
if any([name.startswith("/bns/") for name in d_jobs_list]):
    if d_jobs_list != sorted(d_jobs_list, key=_bns_task_id):
        raise ValueError(
            f"Unexpected DTENSOR_JOBS content {d_jobs}. Sort entries "
            "in DTENSOR_JOBS because cluster construction relies on "
            "the order.")

exit(d_jobs_list)
