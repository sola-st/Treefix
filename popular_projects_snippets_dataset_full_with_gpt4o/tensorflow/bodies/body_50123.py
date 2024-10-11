# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saving_utils.py
if (not version_utils.is_v1_layer_or_model(model) and
    model.outputs is not None):
    try:
        if not model.compiled_loss.built:
            model.compiled_loss.build(model.outputs)
        if not model.compiled_metrics.built:
            model.compiled_metrics.build(model.outputs, model.outputs)
    except:  # pylint: disable=bare-except
        logging.warning(
            'Compiled the loaded model, but the compiled metrics have yet to '
            'be built. `model.compile_metrics` will be empty until you train '
            'or evaluate the model.')
