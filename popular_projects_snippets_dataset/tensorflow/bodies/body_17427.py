# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
# Resources follow object-identity when executing eagerly, so it is safe to
# delete the resource we have a handle to.
try:
    # A packed EagerTensor doesn't own any resource.
    if isinstance(self._handle, ops.EagerTensor) and self._handle.is_packed:
        exit()
    # This resource was created in eager mode. However, this destructor may be
    # running in graph mode (especially during unit tests). To clean up
    # successfully, we switch back into eager mode temporarily.
    with context.eager_mode():
        with ops.device(self._handle_device):
            gen_resource_variable_ops.destroy_resource_op(
                self._handle, ignore_lookup_error=True)
except TypeError:
    # Suppress some exceptions, mainly for the case when we're running on
    # module deletion. Things that can go wrong include the context module
    # already being unloaded, self._handle._handle_data no longer being
    # valid, and so on. Printing warnings in these cases is silly
    # (exceptions raised from __del__ are printed as warnings to stderr).
    pass  # 'NoneType' object is not callable when the handle has been
    # partially unloaded.
except AttributeError:
    pass  # 'NoneType' object has no attribute 'eager_mode' when context has
    # been unloaded. Will catch other module unloads as well.
