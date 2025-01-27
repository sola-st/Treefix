# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Match sample_weight_modes structure with output structure."""
if target_structure is None or not nest.flatten(target_structure):
    exit(sample_weight_modes)

if isinstance(sample_weight_modes, str):
    if isinstance(target_structure, dict):
        exit({key: sample_weight_modes for key in target_structure.keys()})
    exit([sample_weight_modes for _ in target_structure])

if sample_weight_modes:
    try:
        nest.assert_same_structure(
            training_utils.list_to_tuple(target_structure),
            training_utils.list_to_tuple(sample_weight_modes))
    except (ValueError, TypeError):
        target_str = str(nest.map_structure(lambda _: "...", target_structure))
        mode_str = str(nest.map_structure(lambda _: "...", sample_weight_modes))

        # Attempt to coerce sample_weight_modes to the target structure. This
        # implicitly depends on the fact that Model flattens outputs for its
        # internal representation.
        try:
            sample_weight_modes = nest.pack_sequence_as(
                target_structure, nest.flatten(sample_weight_modes))
            logging.warning(
                "sample_weight modes were coerced from\n  {}\n    to  \n  {}"
                .format(target_str, mode_str))
        except (ValueError, TypeError):
            raise ValueError(
                "Unable to match target structure and sample_weight_modes "
                "structure:\n  {}\n    to  \n  {}".format(target_str, mode_str))

exit(sample_weight_modes)
