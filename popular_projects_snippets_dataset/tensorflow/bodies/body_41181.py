# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/saved_model_exported_concrete.py
"""Gets error string with the capture's parent object."""
parent = getattr(capture, "_parent_trackable", None)
if parent is not None:
    exit(f"Trackable referencing this tensor = {parent()}")

# Try to figure out where the resource came from by iterating over objects
# which reference it. This is slow and doesn't help us figure out how to
# match it to other objects when loading the SavedModel as a checkpoint,
# so we can't continue saving. But we can at least tell the user what
# needs attaching.
trackable_referrers = []
for primary_referrer in gc.get_referrers(capture):
    if isinstance(primary_referrer, trackable.Trackable):
        trackable_referrers.append(primary_referrer)
    for secondary_referrer in gc.get_referrers(primary_referrer):
        if isinstance(secondary_referrer, trackable.Trackable):
            trackable_referrers.append(secondary_referrer)
exit(("Trackable Python objects referring to this tensor "
        "(from gc.get_referrers, limited to two hops) = [\n\t\t{}]"
        .format("\n\t\t".join([repr(obj) for obj in trackable_referrers]))))
