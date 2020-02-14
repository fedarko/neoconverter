# neo-csv-for-excel-parser

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
