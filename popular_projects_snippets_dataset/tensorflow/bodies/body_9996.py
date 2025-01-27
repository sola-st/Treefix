# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_aot_compile.py
"""Freeze a `MetaGraphDef` in preparation for tfcompile`.

  The graph is always optimized with grappler, and optionally (by default)
  variables are frozen as constants, before compilation happens.

  Args:
    checkpoint_path: Python string.  Path to checkpoints/variables.
    meta_graph_def: Instance of `MetaGraphDef`.
    output_prefix: Python string.  Path prefix for outputs.
    signature_def_key: String, the signature_def to use in the SavedModel.
    variables_to_feed: A list of strings, the variables that will be fed by the
      user; these won't be frozen.  If `None`, then we will extract all the
      variables in the graph and mark them as to-feed.  The default behavior is
      an empty tuple: all variables must be frozen.
  Returns:
    a pair containing the path to the frozen model and the path to the config.
  Raises:
    RuntimeError: If tensorflow was not built with XLA.
    ImportError: If tensorflow was built with XLA but there was another
      issue importing the tfcompile python wrapper.
    ValueError: If `meta_graph_def.signature_def[signature_def_key]` is
      missing or has empty outputs.
  """
if _pywrap_tfcompile_import_error:
    raise _pywrap_tfcompile_import_error  # pylint: disable=raising-bad-type

signature_def_map = meta_graph_def.signature_def
if signature_def_key not in signature_def_map:
    raise ValueError(
        f"Unable to find signature_def_key '{signature_def_key}' in signature "
        'def map of `meta_graph_def`. Available keys: '
        f'{list(signature_def_map.keys())}')
signature_def = signature_def_map[signature_def_key]
if not signature_def.outputs:
    raise ValueError(
        f'Signature key {signature_def_key} must have outputs, but saw none:\n'
        f'{str(signature_def)}')

file_io.recursive_create_dir(output_prefix)
if logging.get_verbosity() >= logging.INFO:
    original_graph_def_location = os.path.join(output_prefix,
                                               'original_graph.pb')
    with file_io.FileIO(original_graph_def_location, 'wb') as graph_writer:
        graph_writer.write(meta_graph_def.graph_def.SerializeToString())

  # This updates graph_def in place.
_replace_input_placeholders_with_default_values(
    meta_graph_def.graph_def, signature_def)

graph_def = _optimize_graph(meta_graph_def, signature_def)

all_variables = _get_variable_nodes_from_graph_def(graph_def)
if variables_to_feed is None:
    variable_nodes_to_feed = list(all_variables.values())
else:
    not_in_graph = set(variables_to_feed).difference(list(all_variables))
    if not_in_graph:
        raise ValueError('Asked to feed variables that were not found in graph: '
                         f'{not_in_graph}. Variables contained in the graph: '
                         f'{list(all_variables)}')
    variable_nodes_to_feed = [
        all_variables[name] for name in variables_to_feed
    ]

if logging.get_verbosity() >= logging.INFO:
    prefrozen_graph_def_location = os.path.join(output_prefix,
                                                'prefrozen_graph.pb')
    with file_io.FileIO(prefrozen_graph_def_location, 'wb') as graph_writer:
        graph_writer.write(graph_def.SerializeToString())

  # Load the Variables so that we can freeze the graph.
with session.Session(graph=ops_lib.Graph()) as sess:
    restorer = saver_lib.import_meta_graph(meta_graph_def, clear_devices=True)
    if restorer is not None:
        restorer.restore(sess, checkpoint_path)
    graph_def.CopyFrom(
        graph_util.convert_variables_to_constants(
            sess,
            graph_def,
            output_node_names=[
                _parse_tensor_name(n.name)[0]
                for n in signature_def.outputs.values()
            ],
            variable_names_blacklist=[
                n.name for n, _ in variable_nodes_to_feed
            ],
        ))

signature_def = _prune_removed_feed_nodes(signature_def, graph_def)

frozen_graph_def_location = os.path.join(output_prefix, 'frozen_graph.pb')
config_pbtxt_location = os.path.join(output_prefix, 'config.pbtxt')
logging.info('Writing graph def to: {}'.format(frozen_graph_def_location))
with file_io.FileIO(frozen_graph_def_location, 'wb') as graph_writer:
    graph_writer.write(graph_def.SerializeToString())
config = _signature_to_tf2xla_config(
    signature_def, variable_nodes_to_feed=variable_nodes_to_feed)
logging.info('Writing config_pbtxt to: {}'.format(config_pbtxt_location))
with file_io.FileIO(config_pbtxt_location, mode='w') as config_writer:
    config_writer.write(str(config))
exit((frozen_graph_def_location, config_pbtxt_location))
