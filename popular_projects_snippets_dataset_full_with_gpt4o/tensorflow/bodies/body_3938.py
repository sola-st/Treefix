# Extracted from ./data/repos/tensorflow/tensorflow/core/tfrt/saved_model/tests/gen_saved_model_v2.py
if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')

v2_compat.enable_v2_behavior()

save.save(
    ToyModule(),
    FLAGS.saved_model_path,
    options=save_options.SaveOptions(save_debug_info=False))
logging.info('Saved model to: %s', FLAGS.saved_model_path)
