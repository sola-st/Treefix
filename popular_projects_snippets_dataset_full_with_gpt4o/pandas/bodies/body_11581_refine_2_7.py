import pytest # pragma: no cover
import pandas as pd # pragma: no cover
from unittest import mock # pragma: no cover

tm = type('Mock', (object,), {'ensure_clean': mock.MagicMock(return_value=mock.MagicMock(__enter__=lambda s: 'test.xml', __exit__=mock.Mock()))})() # pragma: no cover
geom_df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}) # pragma: no cover

import pytest # pragma: no cover
import pandas as pd # pragma: no cover
from unittest import mock # pragma: no cover
from lxml.etree import XSLTApplyError # pragma: no cover

tm = type('Mock', (object,), {'ensure_clean': mock.MagicMock(return_value=mock.MagicMock(__enter__=lambda s: 'test.xml', __exit__=mock.Mock()))})() # pragma: no cover
geom_df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}) # pragma: no cover
original_to_xml = pd.DataFrame.to_xml # pragma: no cover
def failing_to_xml(self, path, stylesheet=None): raise XSLTApplyError('Cannot resolve URI') # pragma: no cover
pd.DataFrame.to_xml = failing_to_xml # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from l3.Runtime import _l_
try:
    from lxml.etree import XSLTApplyError
    _l_(21714)

except ImportError:
    pass

xsl = """\
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" encoding="utf-8" indent="yes" />
    <xsl:strip-space elements="*"/>

    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:copy-of select="document('non_existent.xml')/*"/>
        </xsl:copy>
    </xsl:template>
</xsl:stylesheet>"""
_l_(21715)

with pytest.raises(XSLTApplyError, match=("Cannot resolve URI")):
    _l_(21718)

    with tm.ensure_clean("test.xml") as path:
        _l_(21717)

        geom_df.to_xml(path, stylesheet=xsl)
        _l_(21716)
