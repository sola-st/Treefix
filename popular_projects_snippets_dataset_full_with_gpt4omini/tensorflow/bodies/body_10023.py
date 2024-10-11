# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Runs SavedModel and fetch all outputs.

  Runs the input dictionary through the MetaGraphDef within a SavedModel
  specified by the given tag_set and SignatureDef. Also save the outputs to file
  if outdir is not None.

  Args:
    saved_model_dir: Directory containing the SavedModel to execute.
    tag_set: Group of tag(s) of the MetaGraphDef with the SignatureDef map, in
        string format, separated by ','. For tag-set contains multiple tags, all
        tags must be passed in.
    signature_def_key: A SignatureDef key string.
    input_tensor_key_feed_dict: A dictionary maps input keys to numpy ndarrays.
    outdir: A directory to save the outputs to. If the directory doesn't exist,
        it will be created.
    overwrite_flag: A boolean flag to allow overwrite output file if file with
        the same name exists.
    worker: If provided, the session will be run on the worker.  Valid worker
        specification is a bns or gRPC path.
    init_tpu: If true, the TPU system will be initialized after the session
        is created.
    use_tfrt: If true, TFRT session will be used.
    tf_debug: A boolean flag to use TensorFlow Debugger (TFDBG) to observe the
        intermediate Tensor values and runtime GraphDefs while running the
        SavedModel.

  Raises:
    ValueError: When any of the input tensor keys is not valid.
    RuntimeError: An error when output file already exists and overwrite is not
    enabled.
  """
# Get a list of output tensor names.
meta_graph_def = saved_model_utils.get_meta_graph_def(saved_model_dir,
                                                      tag_set)

# Re-create feed_dict based on input tensor name instead of key as session.run
# uses tensor name.
inputs_tensor_info = _get_inputs_tensor_info_from_meta_graph_def(
    meta_graph_def, signature_def_key)

# Check if input tensor keys are valid.
for input_key_name in input_tensor_key_feed_dict.keys():
    if input_key_name not in inputs_tensor_info:
        raise ValueError(
            '"%s" is not a valid input key. Please choose from %s, or use '
            '--show option.' %
            (input_key_name, '"' + '", "'.join(inputs_tensor_info.keys()) + '"'))

inputs_feed_dict = {
    inputs_tensor_info[key].name: tensor
    for key, tensor in input_tensor_key_feed_dict.items()
}
# Get outputs
outputs_tensor_info = _get_outputs_tensor_info_from_meta_graph_def(
    meta_graph_def, signature_def_key)
# Sort to preserve order because we need to go from value to key later.
output_tensor_keys_sorted = sorted(outputs_tensor_info.keys())
output_tensor_names_sorted = [
    outputs_tensor_info[tensor_key].name
    for tensor_key in output_tensor_keys_sorted
]

config = None
if use_tfrt:
    logging.info('Using TFRT session.')
    config = config_pb2.ConfigProto(
        experimental=config_pb2.ConfigProto.Experimental(use_tfrt=True))
with session.Session(worker, graph=ops_lib.Graph(), config=config) as sess:
    if init_tpu:
        print('Initializing TPU System ...')
        # This is needed for freshly started worker, or if the job
        # restarts after a preemption.
        sess.run(tpu.initialize_system())

    loader.load(sess, tag_set.split(','), saved_model_dir)

    if tf_debug:
        sess = local_cli_wrapper.LocalCLIDebugWrapperSession(sess)

    outputs = sess.run(output_tensor_names_sorted, feed_dict=inputs_feed_dict)

    for i, output in enumerate(outputs):
        output_tensor_key = output_tensor_keys_sorted[i]
        print('Result for output key %s:\n%s' % (output_tensor_key, output))

        # Only save if outdir is specified.
        if outdir:
            # Create directory if outdir does not exist
            if not os.path.isdir(outdir):
                os.makedirs(outdir)
            output_full_path = os.path.join(outdir, output_tensor_key + '.npy')

            # If overwrite not enabled and file already exist, error out
            if not overwrite_flag and os.path.exists(output_full_path):
                raise RuntimeError(
                    'Output file %s already exists. Add \"--overwrite\" to overwrite'
                    ' the existing output files.' % output_full_path)

            np.save(output_full_path, output)
            print('Output %s is saved to %s' % (output_tensor_key,
                                                output_full_path))
