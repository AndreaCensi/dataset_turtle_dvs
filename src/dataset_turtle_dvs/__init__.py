
from procgraph import pg_add_this_package_models
pg_add_this_package_models(__file__, __package__)

from .utils_poses import *
from .utils_aer import *
from .utils_images import *
from .utils_imu import *


def jobs_comptests(context):
    from conf_tools import GlobalConfig
    GlobalConfig.global_load_dirs(['dataset_turtle_dvs.configs'])

    # Our tests are its tests with our configuration
    from rawlogs import unittests

    from comptests import jobs_registrar
    from rawlogs import get_rawlogs_config
    jobs_registrar(context, get_rawlogs_config())

