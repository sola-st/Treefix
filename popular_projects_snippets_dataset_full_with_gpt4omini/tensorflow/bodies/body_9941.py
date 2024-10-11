# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/import_pb_to_tensorboard.py
"""View an SavedModel as a graph in Tensorboard.

  Args:
    model_dir: The directory containing the SavedModel to import.
    log_dir: The location for the Tensorboard log to begin visualization from.
    tag_set: Group of tag(s) of the MetaGraphDef to load, in string format,
      separated by ','. For tag-set contains multiple tags, all tags must be
      passed in.
  Usage: Call this function with your SavedModel location and desired log
    directory. Launch Tensorboard by pointing it to the log directory. View your
    imported SavedModel as a graph.
  """
with session.Session(graph=ops.Graph()) as sess:
    input_graph_def = saved_model_utils.get_meta_graph_def(model_dir,
                                                           tag_set).graph_def
    importer.import_graph_def(input_graph_def)

    pb_visual_writer = summary.FileWriter(log_dir)
    pb_visual_writer.add_graph(sess.graph)
    print("Model Imported. Visualize by running: "
          "tensorboard --logdir={}".format(log_dir))
