from setuptools import find_packages, setup

setup(
    name="geometry_lib",
    packages=find_packages(include=["geometry_lib"]),
    version="0.1.0",
    description="Geometry library with common geometric shapes.",
    author="Aleksandr Mamonov",
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    test_suite="tests",
)
