import os
import pandas as pd
from neoconverter.convert import _convert_one_file


def test_convert_easy():
    fp = os.path.join(
        "neoconverter",
        "tests",
        "inputs",
        "MY1DMM_CHLORA_2016-01-01_rgb_3600x1800.SS.CSV",
    )
    twocoldf = _convert_one_file(fp)
    # The same "cell" values are still here, but now they're just organized
    # one-dimensionally
    assert len(twocoldf.index) == (3600 * 1800)
    assert twocoldf.columns == ["Values"]

    our_df = pd.read_csv(fp, sep=",", dtype=str)
    our_df.set_index(our_df.columns[0], inplace=True)

    def check_row(row_in_twocoldf):
        lat, lon = row_in_twocoldf.name.split(",")
        assert row_in_twocoldf["Values"] == our_df.at[str(lat), lon]

    twocoldf.apply(check_row, axis=1)
