# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util.py
"""Warm-starts a model using the given settings.

  If you are using a tf.estimator.Estimator, this will automatically be called
  during training.

  Args:
    ckpt_to_initialize_from: [Required] A string specifying the directory with
      checkpoint file(s) or path to checkpoint from which to warm-start the
      model parameters.
    vars_to_warm_start: [Optional] One of the following:

      - A regular expression (string) that captures which variables to
        warm-start (see tf.compat.v1.get_collection).  This expression will only
        consider variables in the TRAINABLE_VARIABLES collection -- if you need
        to warm-start non_TRAINABLE vars (such as optimizer accumulators or
        batch norm statistics), please use the below option.
      - A list of strings, each a regex scope provided to
        tf.compat.v1.get_collection with GLOBAL_VARIABLES (please see
        tf.compat.v1.get_collection).  For backwards compatibility reasons,
        this is separate from the single-string argument type.
      - A list of Variables to warm-start.  If you do not have access to the
        `Variable` objects at the call site, please use the above option.
      - `None`, in which case only TRAINABLE variables specified in
        `var_name_to_vocab_info` will be warm-started.

      Defaults to `'.*'`, which warm-starts all variables in the
      TRAINABLE_VARIABLES collection.  Note that this excludes variables such
      as accumulators and moving statistics from batch norm.
    var_name_to_vocab_info: [Optional] Dict of variable names (strings) to
      `tf.estimator.VocabInfo`. The variable names should be "full" variables,
      not the names of the partitions.  If not explicitly provided, the variable
      is assumed to have no (changes to) vocabulary.
    var_name_to_prev_var_name: [Optional] Dict of variable names (strings) to
      name of the previously-trained variable in `ckpt_to_initialize_from`. If
      not explicitly provided, the name of the variable is assumed to be same
      between previous checkpoint and current model.  Note that this has no
      effect on the set of variables that is warm-started, and only controls
      name mapping (use `vars_to_warm_start` for controlling what variables to
      warm-start).

  Raises:
    ValueError: If the WarmStartSettings contains prev_var_name or VocabInfo
      configuration for variable names that are not used.  This is to ensure
      a stronger check for variable configuration than relying on users to
      examine the logs.
  """
logging.info("Warm-starting from: {}".format(ckpt_to_initialize_from))
grouped_variables = _get_grouped_variables(vars_to_warm_start)

if var_name_to_vocab_info is None:
    var_name_to_vocab_info = {}

if not var_name_to_prev_var_name:
    # Detect whether the checkpoint is object-based, in which case the
    # var_name_to_prev_var_name dictionary should map variable names to
    # checkpoint keys. If the user has specified var_name_to_prev_var_name, we
    # do not override it.
    var_name_to_prev_var_name = _get_object_checkpoint_renames(
        ckpt_to_initialize_from, grouped_variables.keys())

warmstarted_count = 0

# Keep track of which var_names in var_name_to_prev_var_name and
# var_name_to_vocab_info have been used.  Err on the safer side by throwing an
# exception if any are unused by the end of the loop.  It is easy to misname
# a variable during this configuration, in which case without this check, we
# would fail to warm-start silently.
prev_var_name_used = set()
vocab_info_used = set()

# Group the vocabless vars into one call to init_from_checkpoint.
vocabless_vars = {}
for var_name, variable in grouped_variables.items():
    prev_var_name = var_name_to_prev_var_name.get(var_name)
    if prev_var_name:
        prev_var_name_used.add(var_name)
    vocab_info = var_name_to_vocab_info.get(var_name)
    if vocab_info:
        vocab_info_used.add(var_name)
        warmstarted_count += 1
        logging.debug(
            "Warm-starting variable: {}; current_vocab: {} current_vocab_size: {}"
            " prev_vocab: {} prev_vocab_size: {} current_oov: {} prev_tensor: {}"
            " initializer: {}".format(
                var_name, vocab_info.new_vocab, vocab_info.new_vocab_size,
                vocab_info.old_vocab, (vocab_info.old_vocab_size if
                                       vocab_info.old_vocab_size > 0 else "All"),
                vocab_info.num_oov_buckets, prev_var_name or "Unchanged",
                vocab_info.backup_initializer or "zero-initialized"))
        _warm_start_var_with_vocab(
            variable,
            current_vocab_path=vocab_info.new_vocab,
            current_vocab_size=vocab_info.new_vocab_size,
            prev_ckpt=ckpt_to_initialize_from,
            prev_vocab_path=vocab_info.old_vocab,
            previous_vocab_size=vocab_info.old_vocab_size,
            current_oov_buckets=vocab_info.num_oov_buckets,
            prev_tensor_name=prev_var_name,
            initializer=vocab_info.backup_initializer,
            axis=vocab_info.axis)
    else:
        # For the special value of vars_to_warm_start = None,
        # we only warm-start variables with explicitly specified vocabularies.
        if vars_to_warm_start:
            warmstarted_count += 1
            logging.debug("Warm-starting variable: {}; prev_var_name: {}".format(
                var_name, prev_var_name or "Unchanged"))
            # Because we use a default empty list in grouped_variables, single
            # unpartitioned variables will be lists here, which we rectify in order
            # for init_from_checkpoint logic to work correctly.
            if len(variable) == 1:
                variable = variable[0]
            prev_tensor_name, var = _get_var_info(variable, prev_var_name)
            if prev_tensor_name in vocabless_vars:
                # The API for checkpoint_utils.init_from_checkpoint accepts a mapping
                # from checkpoint tensor names to model variable names, so it does not
                # support warm-starting two variables from the same tensor.  Our work-
                # around is to run init_from_checkpoint multiple times, each time we
                # encounter a new variable that should be initialized by a previously-
                # used tensor.
                logging.debug("Requested prev_var_name {} initialize both {} and {}; "
                              "calling init_from_checkpoint.".format(
                                  prev_tensor_name,
                                  vocabless_vars[prev_tensor_name],
                                  var))
                checkpoint_utils.init_from_checkpoint(ckpt_to_initialize_from,
                                                      vocabless_vars)
                vocabless_vars.clear()
            vocabless_vars[prev_tensor_name] = var

if vocabless_vars:
    checkpoint_utils.init_from_checkpoint(ckpt_to_initialize_from,
                                          vocabless_vars)
prev_var_name_not_used = set(
    var_name_to_prev_var_name.keys()) - prev_var_name_used
vocab_info_not_used = set(var_name_to_vocab_info.keys()) - vocab_info_used

logging.info("Warm-started %d variables.", warmstarted_count)

if prev_var_name_not_used:
    raise ValueError(
        "You provided the following variables in "
        "var_name_to_prev_var_name that were not used: "
        "{0}.  Perhaps you misspelled them?  Here is the list of viable "
        "variable names: {1}".format(prev_var_name_not_used,
                                     grouped_variables.keys()))
if vocab_info_not_used:
    raise ValueError(
        "You provided the following variables in "
        "var_name_to_vocab_info that were not used: {0}. "
        " Perhaps you misspelled them?  Here is the list of viable variable "
        "names: {1}".format(vocab_info_not_used, grouped_variables.keys()))
