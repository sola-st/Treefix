# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
# Test for flaky failures when reading from a parameter server while a
# worker is recovering.
# Place some variables on PSes using distribute_datasets_from_function,
# kill a worker, and continuously poll one of those variables.

model = Model(self.cluster_coord)

# kill the worker after a delay to make sure variable reading runs while
# worker is up, while it's down, and while it restarts
def kill_after_delay():
    time.sleep(3)
    logging.info("Killing worker 0")
    self._cluster.kill_task("worker", 0)
    time.sleep(1)
    logging.info("Restarting worker 0")
    self._cluster.start_task("worker", 0)

kill_thread = threading.Thread(target=kill_after_delay)
kill_thread.start()

model.do_infinite_step.assign(True)
model.schedule_training_functions(1)

num_reads = 0
num_reads_after_restart = 0
read_interval_secs = 0.1
worker_has_stopped = False
# limit runtime of the test: stop after doing a few reads after worker
# is back up, or after a fixed maximum number of reads
while num_reads_after_restart <= 5 and num_reads < 200:
    worker_up = context.check_alive("/job:worker/replica:0/task:0")
    if not worker_up:
        worker_has_stopped = True
    if worker_up and worker_has_stopped:
        num_reads_after_restart += 1

    model.join_training_functions()
    start = time.time()
    while time.time() < start + read_interval_secs:
        model.iterations.read_value()

    num_reads += 1
    # run another epoch
    model.do_infinite_step.assign(True)
    model.schedule_training_functions(1)
