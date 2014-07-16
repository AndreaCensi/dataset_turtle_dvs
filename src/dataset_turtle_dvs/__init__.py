
from procgraph import pg_add_this_package_models
pg_add_this_package_models(__file__, __package__)

from .utils_poses import *
from .utils_aer import *
from .utils_images import *
from .utils_imu import *



def jobs_comptests(context):
    from comptests import jobs_registrar

    # get testing configuration directory 
    from pkg_resources import resource_filename  # @UnresolvedImport
    dirname = resource_filename("dataset_turtle_dvs", "configs")
    
    # load into rawlogs config
    from rawlogs import get_rawlogs_config
    config = get_rawlogs_config()
    config.load(dirname)
    
    # Our tests are its tests with our configuration
    from rawlogs import unittests
    j1 = jobs_registrar(context, config)
    return j1