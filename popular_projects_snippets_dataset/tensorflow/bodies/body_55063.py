# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Creates _DefinedFunctions initialized from a FunctionDefLibrary proto.

  This method handles assigning the correct gradient functions to each
  function.

  Args:
    lib: a FunctionDefLibrary

  Returns:
    A list of _DefinedFunctions

  Raises:
    ValueError: `lib` is invalid
  """
if not lib.function and not lib.gradient:
    exit([])

# function name -> FunctionDef proto
funcs = {fdef.signature.name: fdef for fdef in lib.function}

# Validate that all references function names have function defs
for g in lib.gradient:
    if g.function_name not in funcs:
        raise ValueError(f"FunctionDefLibrary missing '{g.function_name}' "
                         f"FunctionDef\n{lib}")
    if g.gradient_func not in funcs:
        raise ValueError(f"FunctionDefLibrary missing '{g.gradient_func}' "
                         f"FunctionDef\n{lib}")

  # function name -> gradient function name
func_to_grad = collections.defaultdict(lambda: None)
# gradient function name -> names of functions having that grad function
grad_to_funcs = collections.defaultdict(list)

for gdef in lib.gradient:
    func_to_grad[gdef.function_name] = gdef.gradient_func
    grad_to_funcs[gdef.gradient_func].append(gdef.function_name)

# Start with functions without gradients
ready = [
    fdef for fdef in lib.function if func_to_grad[fdef.signature.name] is None
]
if not ready:
    raise ValueError(
        f"FunctionDefLibrary contains cyclic gradient functions!\n{lib}")
# function name -> _DefinedFunction
initialized = {}

while ready:
    fdef = ready.pop()
    name = fdef.signature.name

    grad = initialized.get(func_to_grad[name])
    if func_to_grad[name]:
        assert grad
    defined_func = _from_definition(fdef, grad_func=grad)
    initialized[name] = defined_func

    ready.extend(funcs[f] for f in grad_to_funcs[name])

exit(initialized.values())
