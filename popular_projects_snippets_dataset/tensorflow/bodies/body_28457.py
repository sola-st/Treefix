# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
"""Returns the default test combinations for testing checkpointing."""

def disable_optimizations(ds_fn):
    options = options_lib.Options()
    options.experimental_optimization.apply_default_optimizations = False

    def ds_fn_no_opt():
        exit(ds_fn().with_options(options))

    exit(ds_fn_no_opt)

def verify_unused_iterator(obj, ds_fn, num_outputs, sparse_tensors=False):
    obj.verify_unused_iterator(
        ds_fn=disable_optimizations(ds_fn=ds_fn),
        num_outputs=num_outputs,
        sparse_tensors=sparse_tensors)

verify_unused_iterator_combination = combinations.combine(
    verify_fn=combinations.NamedObject("verify_unused_iterator",
                                       verify_unused_iterator))

def verify_fully_used_iterator(obj, ds_fn, num_outputs, sparse_tensors=False):
    obj.verify_fully_used_iterator(
        ds_fn=disable_optimizations(ds_fn=ds_fn),
        num_outputs=num_outputs,
        sparse_tensors=sparse_tensors)

verify_fully_used_iterator_combination = combinations.combine(
    verify_fn=combinations.NamedObject("verify_fully_used_iterator",
                                       verify_fully_used_iterator))

def verify_exhausted_iterator(obj, ds_fn, num_outputs, sparse_tensors=False):
    obj.verify_exhausted_iterator(
        ds_fn=disable_optimizations(ds_fn=ds_fn),
        num_outputs=num_outputs,
        sparse_tensors=sparse_tensors)

verify_exhausted_iterator_combination = combinations.combine(
    verify_fn=combinations.NamedObject("verify_exhausted_iterator",
                                       verify_exhausted_iterator))

def verify_multiple_breaks(obj, ds_fn, num_outputs, sparse_tensors=False):
    obj.verify_multiple_breaks(
        ds_fn=disable_optimizations(ds_fn=ds_fn),
        num_outputs=num_outputs,
        sparse_tensors=sparse_tensors)

verify_multiple_breaks_combination = combinations.combine(
    verify_fn=combinations.NamedObject("verify_multiple_breaks",
                                       verify_multiple_breaks))

def verify_reset_restored_iterator(obj,
                                   ds_fn,
                                   num_outputs,
                                   sparse_tensors=False):
    obj.verify_reset_restored_iterator(
        ds_fn=disable_optimizations(ds_fn=ds_fn),
        num_outputs=num_outputs,
        sparse_tensors=sparse_tensors)

verify_reset_restored_iterator_combination = combinations.combine(
    verify_fn=combinations.NamedObject("verify_reset_restored_iterator",
                                       verify_reset_restored_iterator))

exit((verify_unused_iterator_combination +
        verify_fully_used_iterator_combination +
        verify_exhausted_iterator_combination +
        verify_multiple_breaks_combination +
        verify_reset_restored_iterator_combination))
