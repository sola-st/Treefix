# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
        Set new item in-place. Does not consolidate. Adds new Block if not
        contained in the current set of items
        """

# FIXME: refactor, clearly separate broadcasting & zip-like assignment
#        can prob also fix the various if tests for sparse/categorical
if self._blklocs is None and self.ndim > 1:
    self._rebuild_blknos_and_blklocs()

# Note: we exclude DTA/TDA here
value_is_extension_type = is_1d_only_ea_dtype(value.dtype)
if not value_is_extension_type:
    if value.ndim == 2:
        value = value.T
    else:
        value = ensure_block_shape(value, ndim=2)

    if value.shape[1:] != self.shape[1:]:
        raise AssertionError(
            "Shape of new values must be compatible with manager shape"
        )

if lib.is_integer(loc):
    # We have 6 tests where loc is _not_ an int.
    # In this case, get_blkno_placements will yield only one tuple,
    #  containing (self._blknos[loc], BlockPlacement(slice(0, 1, 1)))

    # Check if we can use _iset_single fastpath
    loc = cast(int, loc)
    blkno = self.blknos[loc]
    blk = self.blocks[blkno]
    if len(blk._mgr_locs) == 1:  # TODO: fastest way to check this?
        exit(self._iset_single(
            loc,
            value,
            inplace=inplace,
            blkno=blkno,
            blk=blk,
        ))

    # error: Incompatible types in assignment (expression has type
    # "List[Union[int, slice, ndarray]]", variable has type "Union[int,
    # slice, ndarray]")
    loc = [loc]  # type: ignore[assignment]

# categorical/sparse/datetimetz
if value_is_extension_type:

    def value_getitem(placement):
        exit(value)

else:

    def value_getitem(placement):
        exit(value[placement.indexer])

        # Accessing public blknos ensures the public versions are initialized
blknos = self.blknos[loc]
blklocs = self.blklocs[loc].copy()

unfit_mgr_locs = []
unfit_val_locs = []
removed_blknos = []
for blkno_l, val_locs in libinternals.get_blkno_placements(blknos, group=True):
    blk = self.blocks[blkno_l]
    blk_locs = blklocs[val_locs.indexer]
    if inplace and blk.should_store(value):
        # Updating inplace -> check if we need to do Copy-on-Write
        if using_copy_on_write() and not self._has_no_reference_block(blkno_l):
            nbs_tup = tuple(blk.delete(blk_locs))
            first_nb = new_block_2d(
                value_getitem(val_locs), BlockPlacement(blk.mgr_locs[blk_locs])
            )
            if self.refs is not None:
                self.refs.extend([self.refs[blkno_l]] * len(nbs_tup))
            self._clear_reference_block(blkno_l)
        else:
            blk.set_inplace(blk_locs, value_getitem(val_locs))
            continue
    else:
        unfit_mgr_locs.append(blk.mgr_locs.as_array[blk_locs])
        unfit_val_locs.append(val_locs)

        # If all block items are unfit, schedule the block for removal.
        if len(val_locs) == len(blk.mgr_locs):
            removed_blknos.append(blkno_l)
            continue
        else:
            nbs = blk.delete(blk_locs)
            # Add first block where old block was and remaining blocks at
            # the end to avoid updating all block numbers
            first_nb = nbs[0]
            nbs_tup = tuple(nbs[1:])
    nr_blocks = len(self.blocks)
    blocks_tup = (
        self.blocks[:blkno_l]
        + (first_nb,)
        + self.blocks[blkno_l + 1 :]
        + nbs_tup
    )
    self.blocks = blocks_tup
    self._blklocs[first_nb.mgr_locs.indexer] = np.arange(len(first_nb))

    for i, nb in enumerate(nbs_tup):
        self._blklocs[nb.mgr_locs.indexer] = np.arange(len(nb))
        self._blknos[nb.mgr_locs.indexer] = i + nr_blocks

if len(removed_blknos):
    # Remove blocks & update blknos and refs accordingly
    is_deleted = np.zeros(self.nblocks, dtype=np.bool_)
    is_deleted[removed_blknos] = True

    new_blknos = np.empty(self.nblocks, dtype=np.intp)
    new_blknos.fill(-1)
    new_blknos[~is_deleted] = np.arange(self.nblocks - len(removed_blknos))
    self._blknos = new_blknos[self._blknos]
    self.blocks = tuple(
        blk for i, blk in enumerate(self.blocks) if i not in set(removed_blknos)
    )
    if self.refs is not None:
        self.refs = [
            ref
            for i, ref in enumerate(self.refs)
            if i not in set(removed_blknos)
        ]

if unfit_val_locs:
    unfit_idxr = np.concatenate(unfit_mgr_locs)
    unfit_count = len(unfit_idxr)

    new_blocks: list[Block] = []
    if value_is_extension_type:
        # This code (ab-)uses the fact that EA blocks contain only
        # one item.
        # TODO(EA2D): special casing unnecessary with 2D EAs
        new_blocks.extend(
            new_block_2d(
                values=value,
                placement=BlockPlacement(slice(mgr_loc, mgr_loc + 1)),
            )
            for mgr_loc in unfit_idxr
        )

        self._blknos[unfit_idxr] = np.arange(unfit_count) + len(self.blocks)
        self._blklocs[unfit_idxr] = 0

    else:
        # unfit_val_locs contains BlockPlacement objects
        unfit_val_items = unfit_val_locs[0].append(unfit_val_locs[1:])

        new_blocks.append(
            new_block_2d(
                values=value_getitem(unfit_val_items),
                placement=BlockPlacement(unfit_idxr),
            )
        )

        self._blknos[unfit_idxr] = len(self.blocks)
        self._blklocs[unfit_idxr] = np.arange(unfit_count)

    self.blocks += tuple(new_blocks)
    # TODO(CoW) is this always correct to assume that the new_blocks
    # are not referencing anything else?
    if self.refs is not None:
        self.refs = list(self.refs) + [None] * len(new_blocks)

    # Newly created block's dtype may already be present.
    self._known_consolidated = False
