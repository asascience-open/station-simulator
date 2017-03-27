from setuptools import find_packages, setup

def readme():
    with open('README.rst') as f:
        return f.read()

reqs = [line.strip() for line in open('requirements.txt')]

setup(
    name             = "station-simulator",
    version          = '0.0.1',
    description      = 'Tool for generating station CSV data',
    packages         = find_packages(),
    long_description = readme(),
    author           = 'Luke Campbell',
    author_email     = 'luke.campbell@rpsgroup.com',
    url              = 'https://github.com/asascience-open/station-simulator/',
    install_requires = reqs,
    entry_points     = {
        'console_scripts': [
            'station-simulator = station_simulator.cli:main'
        ]
    },
    classifiers      = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering',
    ],
)

