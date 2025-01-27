# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
if os.environ.get('OMP_NUM_THREADS'):
    logging.warning(
        'OMP_NUM_THREADS is no longer used by the default Keras config. '
        'To configure the number of threads, use tf.config.threading APIs.')

config = get_config()
config.allow_soft_placement = True

exit(config)
