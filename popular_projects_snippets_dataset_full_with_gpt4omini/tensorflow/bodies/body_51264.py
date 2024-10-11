# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Exports the MetaGraph proto of the `obj` to a file.

  This function goes through the same procedures saved_model.save goes to
  produce the given object's MetaGraph, then saves it to the given file. It
  skips saving checkpoint information, and is useful when all one wants is the
  graph defining the model.

  Args:
    obj: A trackable object to build the MetaGraph from.
    filename: The file into which to write the MetaGraph.
    signatures: Optional, either a `tf.function` with an input signature
      specified or the result of `f.get_concrete_function` on a
      `@tf.function`-decorated function `f`, in which case `f` will be used to
      generate a signature for the SavedModel under the default serving
      signature key. `signatures` may also be a dictionary, in which case it
      maps from signature keys to either `tf.function` instances with input
      signatures or concrete functions. The keys of such a dictionary may be
      arbitrary strings, but will typically be from the
      `tf.saved_model.signature_constants` module.
    options: Optional, `tf.saved_model.SaveOptions` object that specifies
      options for saving.
  """
options = options or save_options.SaveOptions()
export_dir = os.path.dirname(filename)
meta_graph_def, exported_graph, _, _, _, _ = _build_meta_graph(
    obj, signatures, options)

file_io.atomic_write_string_to_file(
    filename, meta_graph_def.SerializeToString(deterministic=True))

# Save debug info, if requested.
if options.save_debug_info:
    _export_debug_info(exported_graph, export_dir)

# Clean reference cycles so repeated export()s don't make work for the garbage
# collector. Before this point, we need to keep references to captured
# constants in the saved graph.
ops.dismantle_graph(exported_graph)
