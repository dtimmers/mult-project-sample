import os

from setuptools import setup

ml_base_name = "ml.base"
ml_version = os.environ["ML_VERSION"]
requires_test = ['pytest>=5.4']
requires_dev = ['black', 'twine', 'pypiserver', 'passlib']

setup(
    name=ml_base_name,
    version=ml_version,
    namespace_packages=["ml"],
    packages=[ml_base_name],
    install_requires=[
        "scikit-learn>=0.22"
    ],
    extras_require={
        'test': requires_test,
        'dev': requires_test + requires_dev
    }
)
