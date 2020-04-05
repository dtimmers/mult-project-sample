import os
from contextlib import contextmanager
from dataclasses import dataclass
from json import loads as json_loads
from typing import Any, Dict, List, Tuple


@dataclass
class PackageConfig:
    package_name: str
    version: str
    libs: List[Tuple[str, str]]

    @classmethod
    def from_dict(cls, dict_in: Dict[str, Any]):
        # convert libs into proper format
        libs = [tuple(lib_tuple) for lib_tuple in dict_in["libs"]]
        return cls(
            package_name=dict_in["package_name"],
            version=dict_in["version"],
            libs=libs
        )

    @classmethod
    def from_config_file(cls, config_file: str = "package_info.cfg"):
        with open(config_file, 'r') as config:
            config_dict = json_loads(config.read())
            return PackageConfig.from_dict(config_dict)


@contextmanager
def change_wd(wd_tmp: str):
    """
    Temporarily changes the work directory.

    Args:
        wd_tmp: the directory which will be temporarily used as the working directory

    Returns:
        None

    """
    try:
        # save current work dir
        wd_old = os.getcwd()
        os.chdir(wd_tmp)
        yield None
    finally:
        # restore old work dir
        os.chdir(wd_old)
