#! /usr/bin/env python3
from .utils import _read
import pandas as pd
import click


def _convert_one_file(filepath):
    """Returns a DataFrame modified as expected."""
    data = _read(filepath)
    lat_lon = []
    value = []
    # Go through the rows (each representing a latitude)
    for lat, row in data.iterrows():
        # Go through the cols (each representing a longitude)
        for lon, val in row.iteritems():
            lat_lon.append("{},{}".format(lat, lon))
            value.append(val)

    new_data = pd.Series(value, index=lat_lon)
    new_df = pd.DataFrame(data=new_data, columns=["Values"])
    new_df.index.name = "lat_lon"
    return new_df

@click.command()
@click.option(
    "-i",
    "--input-csv-for-excel-file",
    required=True,
    help="Input 'CSV for Excel' filepath.",
    type=str,
)
@click.option(
    "-o",
    "--output-tsv-file",
    required=True,
    help="Output TSV filepath.",
    type=str,
)
def convert(input_csv_for_excel_file, output_tsv_file) -> None:
    """Converts a geographically formatted CSV file to a two-column format.

       In particular, this assumes that the rows correspond to "chunks" of
       latitudes and the columns correspond to "chunks" of longitudes, and that
       the cell values correspond to some variable of interest within that
       latitude/longitude area.

       The output file produced from this is in a much simpler two-column
       format (each row has a lat/lon coordinate and the value in that "chunk")
       which may be easier to analyze.

       PLEASE NOTE this assumes that the rows and columns are labelled with the
       latitude/longitude values -- this requires selecting the "CSV for Excel"
       download option from NEO's website, not the plain "CSV" option.
    """

    converted_df = _convert_one_file(input_csv_for_excel_file)
    converted_df.to_csv(output_tsv_file, header=True, index=True, sep="\t")


if __name__ == "__main__":
    convert()
