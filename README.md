# neoconverter

Converts "CSV for Excel" data files obtained from the
[NASA Earth Observations website](https://neo.sci.gsfc.nasa.gov/) from the
provided CSV format (each row is a "chunk" of latitudes, each column is a
"chunk" of longitudes, and the cell values correspond to some variable of
interest e.g. chlorophyll) to a simpler two-column format where each row
has the lat/lon coordinate for a chunk and the value in that chunk.

## Disclaimer regarding the use of these data files

Per NEO ([source](https://neo.sci.gsfc.nasa.gov/blog/2013/12/23/csv-and-floating-point-geotiffs/)):

> The values that these files contain have been scaled and resampled
> for visualization purposes in NEO and should not be considered for rigorous
> scientific examination. At best they are useful for basic analysis and trend
> detection but if you are interested in conducting research-level science we
> recommend that you use the original source data (which are not hosted by NEO,
> but we can assist you in identifying the source).

## Installation and command-line usage

```bash
# Install the python package
$ pip install git+https://github.com/fedarko/neoconverter.git
$ convert-neo-excel --help
Usage: convert-neo-excel [OPTIONS]

  Converts a geographically formatted CSV file to a two-column format.

  In particular, this assumes that the rows correspond to "chunks" of
  latitudes and the columns correspond to "chunks" of longitudes, and that
  the cell values correspond to some variable of interest within that
  latitude/longitude area.

  The output file produced from this is in a much simpler two-column format
  (each row has a lat/lon coordinate and the value in that "chunk") which
  may be easier to analyze.

  PLEASE NOTE this assumes that the rows and columns are labelled with the
  latitude/longitude values -- this requires selecting the "CSV for Excel"
  download option from NEO's website, not the plain "CSV" option.

Options:
  -i, --input-csv-for-excel-file TEXT
                                  Input 'CSV for Excel' filepath.  [required]
  -o, --output-tsv-file TEXT      Output TSV filepath.  [required]
  --help                          Show this message and exit.
```

## Running tests

You can just run `make test` in the root of the repository. The tests are
really unoptimized, so this will take a few minutes (PRs welcome).

## TODOs for this repo

- Add back functionality that takes in a list of files and converts all of them
  at once
- Add more documentation, examples, etc.
- Travis/CodeCov integration
- Supporting more types of NEO input files?

## Acknowledgements
This code was developed in conjunction with Justin Shaffer ([@justinshaffer](https://github.com/justinshaffer)).

The test data file contained in this repository (in `neoconverter/tests/inputs/MY1DMM_CHLORA_2016-01-01_rgb_3600x1800.SS.CSV`) was obtained from the [NEO's website](https://neo.sci.gsfc.nasa.gov/view.php?datasetId=MY1DMM_CHLORA&year=2016), and contains observed measurements of Chlorophyll concentrations in January 2016 with "0.1 degrees" granularity.
