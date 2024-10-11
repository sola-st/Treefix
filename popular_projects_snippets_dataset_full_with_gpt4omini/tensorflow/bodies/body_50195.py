# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model_experimental.py
"""Exports a model, and optionally saves new vars from the clone model.

  Args:
    mode: A `tf.estimator.ModeKeys` string.
    has_saved_vars: A `boolean` indicating whether the SavedModel has already
      exported variables.
    builder: A `SavedModelBuilder` object.
    model: A `tf.keras.Model` object.
    custom_objects: A dictionary mapping string names to custom classes
      or functions.
    checkpoint_path: String path to checkpoint.
    input_signature: Nested TensorSpec containing the expected inputs. Can be
      `None`, in which case the signature will be inferred from the model.

  Raises:
    ValueError: If the train/eval mode is being exported, but the model does
      not have an optimizer.
  """
compile_clone = (mode != mode_keys.ModeKeys.PREDICT)
if compile_clone and not model.optimizer:
    raise ValueError(
        'Model does not have an optimizer. Cannot export mode %s' % mode)

model_graph = ops.get_default_graph()
with ops.Graph().as_default() as g, backend.learning_phase_scope(
    mode == mode_keys.ModeKeys.TRAIN):

    if input_signature is None:
        input_tensors = None
    else:
        input_tensors = nest.map_structure(create_placeholder, input_signature)

    # Clone the model into blank graph. This will create placeholders for inputs
    # and targets.
    clone = models_lib.clone_and_build_model(
        model, input_tensors=input_tensors, custom_objects=custom_objects,
        compile_clone=compile_clone)

    # Make sure that iterations variable is added to the global step collection,
    # to ensure that, when the SavedModel graph is loaded, the iterations
    # variable is returned by `tf.compat.v1.train.get_global_step()`. This is
    # required for compatibility with the SavedModelEstimator.
    if compile_clone:
        g.add_to_collection(ops.GraphKeys.GLOBAL_STEP, clone.optimizer.iterations)

    # Extract update and train ops from train/test/predict functions.
    train_op = None
    if mode == mode_keys.ModeKeys.TRAIN:
        clone._make_train_function()  # pylint: disable=protected-access
        train_op = clone.train_function.updates_op
    elif mode == mode_keys.ModeKeys.TEST:
        clone._make_test_function()  # pylint: disable=protected-access
    else:
        clone._make_predict_function()  # pylint: disable=protected-access
    g.get_collection_ref(ops.GraphKeys.UPDATE_OPS).extend(clone.state_updates)

    with session.Session().as_default():
        clone_var_list = _get_var_list(clone)
        if has_saved_vars:
            # Confirm all variables in the clone have an entry in the checkpoint.
            status = clone.load_weights(checkpoint_path)
            status.assert_existing_objects_matched()
        else:
            # Confirm that variables between the clone and model match up exactly,
            # not counting optimizer objects. Optimizer objects are ignored because
            # if the model has not trained, the slot variables will not have been
            # created yet.
            # TODO(b/113179535): Replace with trackable equivalence.
            _assert_same_non_optimizer_objects(model, model_graph, clone, g)

            # TODO(b/113178242): Use value transfer for trackable objects.
            clone.load_weights(checkpoint_path)

            # Add graph and variables to SavedModel.
            # TODO(b/113134168): Switch to add_meta_graph_and_variables.
            clone.save_weights(checkpoint_path, save_format='tf', overwrite=True)
            builder._has_saved_variables = True  # pylint: disable=protected-access

        # Add graph to the SavedModel builder.
        builder.add_meta_graph(
            model_utils.EXPORT_TAG_MAP[mode],
            signature_def_map=_create_signature_def_map(clone, mode),
            saver=saver_lib.Saver(
                clone_var_list,
                # Allow saving Models with no variables. This is somewhat odd, but
                # it's not necessarily a bug.
                allow_empty=True),
            init_op=variables.local_variables_initializer(),
            train_op=train_op)
    exit(None)
