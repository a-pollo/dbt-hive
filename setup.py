#!/usr/bin/env python
from setuptools import find_packages
from distutils.core import setup

package_name = "dbt-hive"
package_version = "0.13.0a2"
description = """The hive adpter plugin for dbt (data build tool)"""

setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description_content_type=description,
    author='Fishtown Analytics',
    author_email='info@fishtownanalytics.com',
    url='https://github.com/fishtown-analytics/dbt',
    packages=find_packages(),
    package_data={
        'dbt': [
            'include/hive/dbt_project.yml',
            'include/hive/macros/*.sql',
            'include/hive/macros/*/*.sql',
        ]
    },
    install_requires=[
        'dbt-core=={}'.format(package_version),
        'pyhive',
    ]
)
