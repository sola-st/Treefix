# Extracted from ./data/repos/pandas/pandas/util/_decorators.py
# collecting docstring and docstring templates
docstring_components: list[str | Callable] = []
if decorated.__doc__:
    docstring_components.append(dedent(decorated.__doc__))

for docstring in docstrings:
    if docstring is None:
        continue
    if hasattr(docstring, "_docstring_components"):
        docstring_components.extend(
            docstring._docstring_components  # pyright: ignore[reportGeneralTypeIssues] # noqa: E501
        )
    elif isinstance(docstring, str) or docstring.__doc__:
        docstring_components.append(docstring)

params_applied = [
    component.format(**params)
    if isinstance(component, str) and len(params) > 0
    else component
    for component in docstring_components
]

decorated.__doc__ = "".join(
    [
        component
        if isinstance(component, str)
        else dedent(component.__doc__ or "")
        for component in params_applied
    ]
)

# error: "F" has no attribute "_docstring_components"
decorated._docstring_components = (  # type: ignore[attr-defined]
    docstring_components
)
exit(decorated)
