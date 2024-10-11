# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
values = values.T
ncols = 1 if values.ndim == 1 else values.shape[1]

result: ArrayLike
result = np.zeros(ngroups * ncols, dtype=cython_dtype)
result = result.reshape((ngroups, ncols))

func = partial(base_func, out=result)

inferences = None

if needs_counts:
    counts = np.zeros(self.ngroups, dtype=np.int64)
    func = partial(func, counts=counts)

vals = values
if pre_processing:
    vals, inferences = pre_processing(vals)

vals = vals.astype(cython_dtype, copy=False)
if vals.ndim == 1:
    vals = vals.reshape((-1, 1))
func = partial(func, values=vals)

if how != "std" or isinstance(values, BaseMaskedArray):
    mask = isna(values).view(np.uint8)
    if mask.ndim == 1:
        mask = mask.reshape(-1, 1)
    func = partial(func, mask=mask)

if how != "std":
    is_nullable = isinstance(values, BaseMaskedArray)
    func = partial(func, nullable=is_nullable)

else:
    result_mask = np.zeros(result.shape, dtype=np.bool_)
    func = partial(func, result_mask=result_mask)

func(**kwargs)  # Call func to modify indexer values in place

if values.ndim == 1:
    assert result.shape[1] == 1, result.shape
    result = result[:, 0]

if post_processing:
    pp_kwargs: dict[str, bool | np.ndarray] = {}
    pp_kwargs["nullable"] = isinstance(values, BaseMaskedArray)
    if how == "std":
        pp_kwargs["mask"] = result_mask

    result = post_processing(result, inferences, **pp_kwargs)

exit(result.T)
