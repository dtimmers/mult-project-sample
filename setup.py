import os
from typing import List, Tuple

from pip import main as pip_main
from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

from util import change_wd, PackageConfig

package_config = PackageConfig.from_config_file()
os.environ["ML_VERSION"] = package_config.version


def install_ml_libs(libs: List[Tuple[str, str]], dev_install: bool):
    install_mode = "develop" if dev_install else "normal"
    print(f"Installing all ml libs in {install_mode} mode.")
    for lib_name, lib_dir in libs:
        with change_wd(os.path.join(lib_dir)):
            try:
                if dev_install:
                    pip_main(['install', '-e', '.[dev]'])
                else:
                    pip_main(['install', '.'])
            except Exception as e:
                print(f"Something went wrong installing {lib_name}:\n {e}")


class DevelopCmd(develop):
    """ Add custom steps for the develop command """

    def run(self):
        install_ml_libs(package_config.libs, dev_install=True)
        develop.run(self)


class InstallCmd(install):
    """ Add custom steps for the install command """

    def run(self):
        install_ml_libs(package_config.libs, dev_install=False)
        install.run(self)


setup(
    name=package_config.package_name,
    version=package_config.version,
    author="yourname",
    author_email="yourname@email.com",
    description="Macrolib's description",
    license="TBD",
    cmdclass={
        'install': InstallCmd,
        'develop': DevelopCmd,
    },
)
