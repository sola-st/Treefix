# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/profiler/capture_tpu_profile.py
logging.set_verbosity(logging.INFO)
tf_version = versions.__version__
print('TensorFlow version %s detected' % tf_version)
print('Welcome to the Cloud TPU Profiler v%s' % profiler_version.__version__)

if LooseVersion(tf_version) < LooseVersion('2.2.0'):
    sys.exit('You must install tensorflow >= 2.2.0 to use this plugin.')

if not FLAGS.service_addr and not FLAGS.tpu:
    sys.exit('You must specify either --service_addr or --tpu.')

tpu_cluster_resolver = None
if FLAGS.service_addr:
    if FLAGS.tpu:
        logging.warn('Both --service_addr and --tpu are set. Ignoring '
                     '--tpu and using --service_addr.')
    service_addr = FLAGS.service_addr
else:
    try:
        tpu_cluster_resolver = (
            resolver.TPUClusterResolver([FLAGS.tpu],
                                        zone=FLAGS.tpu_zone,
                                        project=FLAGS.gcp_project))
        service_addr = tpu_cluster_resolver.get_master()
    except (ValueError, TypeError):
        sys.exit('Failed to find TPU %s in zone %s project %s. You may use '
                 '--tpu_zone and --gcp_project to specify the zone and project of'
                 ' your TPU.' % (FLAGS.tpu, FLAGS.tpu_zone, FLAGS.gcp_project))
service_addr = service_addr.replace('grpc://', '').replace(':8470', ':8466')

workers_list = ''
if FLAGS.workers_list is not None:
    workers_list = FLAGS.workers_list
elif tpu_cluster_resolver is not None:
    workers_list = get_workers_list(tpu_cluster_resolver)

# If profiling duration was not set by user or set to a non-positive value,
# we set it to a default value of 1000ms.
duration_ms = FLAGS.duration_ms if FLAGS.duration_ms > 0 else 1000

if FLAGS.monitoring_level > 0:
    print('Since monitoring level is provided, profile', service_addr, ' for ',
          FLAGS.duration_ms, ' ms and show metrics for ', FLAGS.num_queries,
          ' time(s).')
    monitoring_helper(service_addr, duration_ms, FLAGS.monitoring_level,
                      FLAGS.num_queries)
else:
    if not FLAGS.logdir:
        sys.exit('You must specify either --logdir or --monitoring_level.')

    if not gfile.Exists(FLAGS.logdir):
        gfile.MakeDirs(FLAGS.logdir)

    try:
        if LooseVersion(tf_version) < LooseVersion('2.3.0'):
            profiler_client.trace(service_addr, os.path.expanduser(FLAGS.logdir),
                                  duration_ms, workers_list,
                                  FLAGS.num_tracing_attempts)
        else:
            options = profiler.ProfilerOptions(
                host_tracer_level=FLAGS.host_tracer_level)
            profiler_client.trace(service_addr, os.path.expanduser(FLAGS.logdir),
                                  duration_ms, workers_list,
                                  FLAGS.num_tracing_attempts, options)
    except errors.UnavailableError:
        sys.exit(0)
