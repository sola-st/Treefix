# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handler_test.py
if _is_oss():
    rpc_layer = 'grpc'
else:
    rpc_layer = 'grpc+loas'

checkpoint_dir = os.path.join(self.get_temp_dir(), 'fh_ckpt')
gfile.MakeDirs(checkpoint_dir)

save_fn = lambda: print('Do nothing')
termination_config = failure_handling.TerminationConfig(
    save_fn=save_fn)

has_chief = False
cluster_spec = multi_worker_test_base.create_cluster_spec(
    has_chief=has_chief,
    num_workers=CLUSTER_SIZE)
training_started_event = multi_process_runner.manager().Event()

mpr = multi_process_runner.MultiProcessRunner(
    self.worker_fn,
    cluster_spec,
    args=(checkpoint_dir, cluster_spec, 'checkpoint',
          [training_started_event], None, None, None, termination_config),
    rpc_layer=rpc_layer,
    return_output=True,
    dependence_on_chief=has_chief)

logging.info('Cluster starting.')
mpr.start()
while not training_started_event.is_set():
    time.sleep(1)

killed_worker = random.randrange(0, CLUSTER_SIZE)
logging.info('sending SIGTERM')
os.kill(mpr.get_process_id('worker', killed_worker), signal.SIGTERM)
logging.info('SIGTERM sent')

# 5 is the grace period length
raise_if_not_all_exit(5, mpr)

match_group = [
    re.search(r'.*ckpt-(\d+).index', a_file)
    for a_file in gfile.ListDirectory(checkpoint_dir)
]

# By default, as tested by other test cases, checkpoint will be saved.
# This passed in save_fn skips it.
self.assertEmpty(match_group)
