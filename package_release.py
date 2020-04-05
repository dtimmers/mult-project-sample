import os

from util import change_wd, PackageConfig

package_config = PackageConfig.from_config_file()
os.environ["ML_VERSION"] = package_config.version


def release_package(lib_name: str, lib_dir: str, repository: str = "internal"):
    root = os.getcwd()
    with change_wd(lib_dir):
        try:
            # build distribution
            os.system("python setup.py sdist bdist_wheel")
            # upload package
            os.system(f"twine upload --config-file {root}/.pypirc -r {repository} dist/*")
        except Exception as e:
            print(f"Something went wrong relaasing {lib_name}:\n {e}")


# release the libraries
for lib_name, lib_dir in package_config.libs:
    release_package(lib_name, lib_dir)

# release the complete library
release_package(package_config.package_name, ".")
