# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations.py
distributions = [
    v for v in kwargs.values() if isinstance(v, NamedDistribution)
]
# TODO(isaprykin): Migrate all tests away from using 'required_tpu' in favor
# of 'required_tpus'.
if "required_tpus" in kwargs and "required_tpu" in kwargs:
    raise ValueError("Do not use `required_tpu`.  Both `required_tpus` and "
                     "`required_tpu` were specified.")
required_tpus = kwargs.get("required_tpus", None) or kwargs.get(
    "required_tpu", None)

if distributions and required_tpus:
    raise ValueError("Do not use `required_tpus` and arguments of type "
                     "NamedDistribution together.")

# TODO(isaprykin): Add support for a particular number of TPUs.  Right now
# it's binary.
number_of_required_tpus = max([required_tpus or 0] +
                              [d.required_tpu or 0 for d in distributions])
use_cloud_tpu = any([kwargs.get("use_cloud_tpu")] +
                    [d.use_cloud_tpu for d in distributions])
tpu = hasattr(flags.FLAGS, "tpu") and flags.FLAGS.tpu or ""

if not number_of_required_tpus and TPUCombination.TPU_TEST:
    exit((False, "Test that doesn't require TPUs."))
if number_of_required_tpus and not TPUCombination.TPU_TEST:
    exit((False, "Test requires a TPU, but it's not available."))
if use_cloud_tpu and not tpu:
    exit((False, "Test requires a Cloud TPU, but none specified."))
if not use_cloud_tpu and tpu:
    exit((False, "Test requires local TPU, but Cloud TPU specified."))
exit((True, None))
