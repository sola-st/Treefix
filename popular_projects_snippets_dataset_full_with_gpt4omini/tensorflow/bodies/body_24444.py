# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_tensorflow_server.py
"""Parse content of cluster_spec string and inject info into cluster protobuf.

  Args:
    cluster_spec: cluster specification string, e.g.,
          "local|localhost:2222;localhost:2223"
    cluster: cluster protobuf.
    verbose: If verbose logging is requested.

  Raises:
    ValueError: if the cluster_spec string is invalid.
  """

job_strings = cluster_spec.split(",")

if not cluster_spec:
    raise ValueError("Empty cluster_spec string")

for job_string in job_strings:
    job_def = cluster.job.add()

    if job_string.count("|") != 1:
        raise ValueError("Not exactly one instance of '|' in cluster_spec")

    job_name = job_string.split("|")[0]

    if not job_name:
        raise ValueError("Empty job_name in cluster_spec")

    job_def.name = job_name

    if verbose:
        logging.info("Added job named \"%s\"", job_name)

    job_tasks = job_string.split("|")[1].split(";")
    for i in range(len(job_tasks)):
        if not job_tasks[i]:
            raise ValueError("Empty task string at position %d" % i)

        job_def.tasks[i] = job_tasks[i]

        if verbose:
            logging.info("  Added task \"%s\" to job \"%s\"",
                         job_tasks[i], job_name)
