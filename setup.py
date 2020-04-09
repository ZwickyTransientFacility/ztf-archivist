from setuptools import setup

# requirements
install_requires = [
    "confluent_kafka",
]

dev_requires = [
    "black",
    "flake8",
    "pytest",
]

setup(
    name="ztf-archivist",
    version="0.1.0",
    description="Archives ZTF data for later access",
    url="https://github.com/dirac-institute/ztf-archivist",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 3 - Alpha",
        "Operating System :: POSIX :: Linux",
    ],
    author="Spencer Nelson",
    author_email="swnelson@uw.edu",
    license="BSD",
    packages=[],
    scripts=["bin/ztf-archivist"],
    install_requires=install_requires,
    extras_require={"dev": dev_requires,},
)
