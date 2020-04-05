import os

from setuptools import setup

ml_pytorch_name = "ml.pytorch"
ml_version = os.environ["ML_VERSION"]

setup(
    name=ml_pytorch_name,
    version=ml_version,
    namespace_packages=["ml"],
    packages=[ml_pytorch_name],
    install_requires=[
        f"ml.base=={ml_version}",
        "torch>=1.4",
    ],
    extras_require={
        "dev": ["pdoc3"]
    },
)
