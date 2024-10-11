import pytest # pragma: no cover
import os # pragma: no cover
import tempfile # pragma: no cover
import pandas as pd # pragma: no cover
from lxml import etree # pragma: no cover

tm = tempfile.NamedTemporaryFile # pragma: no cover
geom_df = pd.DataFrame({'data': [1, 2, 3]}) # pragma: no cover

import pytest # pragma: no cover
import tempfile # pragma: no cover
import pandas as pd # pragma: no cover
from lxml.etree import XSLTApplyError # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from l3.Runtime import _l_
try:
    from lxml.etree import XSLTApplyError
    _l_(10450)

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
_l_(10451)

with pytest.raises(XSLTApplyError, match=("Cannot resolve URI")):
    _l_(10454)

    with tm.ensure_clean("test.xml") as path:
        _l_(10453)

        geom_df.to_xml(path, stylesheet=xsl)
        _l_(10452)
