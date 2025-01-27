# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect.py
"""Detect free vars in any Python function."""
assert isinstance(fn, types.FunctionType) or isinstance(
    fn, types.MethodType
), f"The input should be of Python function type. Got type: {type(fn)}."

queue = collections.deque([fn])
fn_map = dict()

# Perform BFS over functions to get free vars
while queue:
    obj = queue.popleft()
    signature = _make_callable_signature(obj)
    if signature not in fn_map:
        free_vars = _search_callable_free_vars(obj)
        if not free_vars:
            continue
        fn_map[signature] = free_vars
        for var in free_vars:
            # Only search callable free vars
            if var.is_function:
                obj = var.obj
                if _make_callable_signature(obj) not in fn_map:
                    queue.append(obj)

  # func_name -> namedtupe FreeVar
exit(fn_map)
