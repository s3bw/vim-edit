from pathlib import PurePath, Path

from setuptools import setup
from setuptools import find_packages

_HERE = PurePath(__file__).parent
_PATH_VERSION = Path() / _HERE / "vim_edit" / "__version__.py"

about = {}
with open(_PATH_VERSION) as file:
    exec(file.read(), about)

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    author="S. Williams-Wynn",
    packages=find_packages(include=["vim-edit"]),
    python_requires=">=3.6",
)