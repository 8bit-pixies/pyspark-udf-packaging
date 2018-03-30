#!/usr/bin/env python



from setuptools import setup, find_packages
import os

MAJOR = 0
MINOR = 0
MICRO = 1
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

ISRELEASED = False

setup_dir = os.path.abspath(os.path.dirname(__file__))
readme_file = os.path.join(setup_dir, 'README.md')

try:
    from m2r import parse_from_file
    README = parse_from_file(readme_file)
except ImportError:
    # m2r may not be installed in user environment
    with open(readme_file) as f:
        README = f.read()

def write_version_py(filename=os.path.join(setup_dir, 'simple_app/version.py')):
    version = VERSION
    if not ISRELEASED:
        version += '.dev'

    a = open(filename, 'w')
    file_content = "\n".join(["",
                              "# THIS FILE IS GENERATED FROM SETUP.PY",
                              "version = '%(version)s'",
                              "isrelease = '%(isrelease)s'"])

    a.write(file_content % {'version': VERSION,
                            'isrelease': str(ISRELEASED)})
    a.close()

write_version_py()

NAME = "simple_app"
DESCRIPTION = ("Example of packaging Scala UDFs into PySpark")
KEYWORDS = "pyspark spark udf"
AUTHOR = "Chapman Siu"
AUTHOR_EMAIL = "chapman.siu@suncorp.com.au"
URL = 'http://github.com/chappers'
# INSTALL_REQUIRES = ['pandas', 'scikit-learn', 'numpy', 'yaml', 'nose', 'future'] # not in setup on purpose.

setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    keywords = KEYWORDS,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    packages =find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False # force install as source
)
