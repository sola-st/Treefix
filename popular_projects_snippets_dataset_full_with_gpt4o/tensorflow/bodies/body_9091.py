# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
if self.extended.experimental_should_init is None:
    if task_id == 0:
        self.extended.experimental_should_init = True
    else:
        self.extended.experimental_should_init = False
if self.extended.should_checkpoint is None:
    if task_id == 0:
        self.extended.should_checkpoint = True
    else:
        self.extended.should_checkpoint = False
if self.extended.should_save_summary is None:
    if task_id == 0:
        self.extended.should_save_summary = True
    else:
        self.extended.should_save_summary = False

if session_config:
    if (cluster_spec and task_type and task_id is not None and
        self.extended.experimental_between_graph):
        session_config.intra_op_parallelism_threads += 1
        if task_type in ["chief", "worker"]:
            session_config.device_filters.extend(
                ["/job:%s/task:%d" % (task_type, task_id), "/job:ps"])
    else:
        session_config.inter_op_parallelism_threads += 1
        session_config.device_filters.append("/job:somejob")
