import os
import pytest
import pandas as pd
from neoconverter.convert import _convert_one_file
from neoconverter.utils import _read

def test_read():
    fp = os.path.join(
        "neoconverter", "tests", "inputs",
        "MY1DMM_CHLORA_2016-01-01_rgb_3600x1800.SS.CSV"
    )
    df = _read(fp)
    assert len(df.columns) == 3600
    assert len(df.index) == 1800
