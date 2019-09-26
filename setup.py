from setuptools import setup, find_packages


def read_file(filename):
    with open(filename) as f:
        return f.read()


setup(
    python_requires="~=3.7",
    name="python-either",
    version=read_file("./python_either/VERSION").strip(),
    description="Python either monad",
    long_description=read_file("README.md"),
    author="Kirmanie L Ravariere",
    author_email="enamrik@gmail.com",
    url="https://github.com/enamrik/python-either",
    license=read_file("LICENSE"),
    packages=find_packages(exclude=("tests", "outputs")),
    package_data={"python_either": ["VERSION", "*.txt", "*.yml", "*.template", "*.ini", "bin/**/*"]},
    include_package_data=True,
    install_requires=[],
    extras_require={
        'dev': ['pytest']
    },
)
