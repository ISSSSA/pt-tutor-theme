import io
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))




def load_about():
    about = {}
    with io.open(
        os.path.join(HERE, "ptt", "__about__.py"),
        "rt",
        encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()


setup(
    name="ptt",
    version=ABOUT["__version__"],
    url="https://github.com/ISSSSA/ptt",
    project_urls={
        "Documentation": "https://docs.tutor.edly.io/",
        "Code": "https://github.com/ISSSSA/ptt",
        "Issue tracker": "https://github.com/ISSSSA/ptt/issues",
        "Community": "https://discuss.openedx.org",
    },
    license="AGPLv3",
    author="Overhang.IO",
    author_email="contact@overhang.io",
    maintainer="Edly",
    maintainer_email="hina.khadim@arbisoft.com",
    description="ptt theme plugin for Tutor",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=["tutor>=18.0.0,<19.0.0", "tutor-mfe>=18.0.0,<19.0.0"],
    extras_require={"dev": "tutor[dev]>=18.0.0,<19.0.0"},
    entry_points={"tutor.plugin.v1": ["ptt = ptt.plugin"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
