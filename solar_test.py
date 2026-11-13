import xarray
import xradio
import pathlib
import dougu
import toolviper

from xradio.measurement_set import open_processing_set
#from xradio._utils.zarr.config import ZARR_FORMAT

directory = pathlib.Path.cwd()
ps_file = directory.joinpath("data/uid___A002_Xc1469f_X1c33.ps.zarr")
ps_xdt = open_processing_set(str(ps_file))

#ps_xdt.xr_ps.query(scan_intents="OBSERVE_TARGET#OFF_SOURCE")
ps_xdt["uid___A002_Xc1469f_X1c33_00"].xr_ms.get_partition_info()
