from typing import List, Union
import libcst as cst
from libcst._flatten_sentinel import FlattenSentinel
from libcst._nodes.statement import BaseStatement, If
from libcst._removal_sentinel import RemovalSentinel
from libcst.metadata import (
    ParentNodeProvider,
    PositionProvider,
)
import libcst.matchers as m

class RemoveLines(m.MatcherDecoratableTransformer):
    lines_to_keep: List[int]
    METADATA_DEPENDENCIES = (
        ParentNodeProvider,
        PositionProvider,
    )

    def __init__(self, lines_to_remove):
        super().__init__()
        print(lines_to_remove)
        self.lines_to_remove = lines_to_remove

    def on_leave(self, original_node, updated_node) -> Union[BaseStatement, FlattenSentinel[BaseStatement], RemovalSentinel]:
        if isinstance(original_node, BaseStatement) or isinstance(original_node, cst.Comment):
            location = self.get_metadata(PositionProvider, original_node)
            if location.start.line in self.lines_to_remove:
                return cst.RemoveFromParent()

        return updated_node