# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/offline_analyzer.py
if FLAGS.log_usage:
    pass  # No logging for open-source.

if not FLAGS.dump_dir:
    print("ERROR: dump_dir flag is empty.", file=sys.stderr)
    sys.exit(1)

print("tfdbg offline: FLAGS.dump_dir = %s" % FLAGS.dump_dir)

debug_dump = debug_data.DebugDumpDir(
    FLAGS.dump_dir, validate=FLAGS.validate_graph)
cli = analyzer_cli.create_analyzer_ui(
    debug_dump,
    tensor_filters={"has_inf_or_nan": debug_data.has_inf_or_nan},
    ui_type=FLAGS.ui_type)

title = "tfdbg offline @ %s" % FLAGS.dump_dir
cli.run_ui(title=title, title_color="black_on_white", init_command="lt")
