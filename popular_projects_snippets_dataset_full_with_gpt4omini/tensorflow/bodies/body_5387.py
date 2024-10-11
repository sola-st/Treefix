# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Update a SavedObject proto for the caller.

    If a DistributedVariable object supports this method, it will be called when
    saving with a pre-built `SavedObject` proto representing the object, plus an
    instance of `SaveOptions`. This method is then free to modify that proto
    instance.

    `DistributedVariable` with `AUTO` or `ON_WRITE` synchronization optionally
    write out information about their components to the
    `experimental_distributed_variable_components` field of a
    `SavedVariable` (depending on the `SaveOptions` variable policy).

    Args:
      var : A DistributedVariable object
      proto: A pre-built `SavedObject` proto for this object. It is assumed this
        will be a `SavedVariable` instance.
      options: A `SaveOptions` instance.
    """
values_util.write_object_proto(var, proto, options)
