# by-n-they-come Copyright © 2021 Aaron Seilis. See LICENSE for details.

from setuptools import setup

setup(
    name="by-n-they-come",
    author="Aaron Seilis <aaron.seilis@seilis.ca>",
    version="1.0.0",
    packages=["byntheycome"],
    entry_points={
        "console_scripts": [
            "by-n-they-come = byntheycome.lib:main"
        ]
    },
    license="GPLv3+",
)
