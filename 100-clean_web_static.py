#!/usr/bin/python3
"""
Deletes out-of-date archives
"""

import os
from fabric.api import *

env.hosts = ['54.90.33.112', '23.23.75.134']


def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = 1 if int(number) == 0 else int(number)

    # Clean local archives
    with lcd("versions"):
        local("ls -1t web_static_*.tgz | tail -n +{} | xargs -r rm -f"
              .format(number + 1))

    # Clean remote archives
    with cd("/data/web_static/releases"):
        run("ls -1t | grep 'web_static_' | tail -n +{} | xargs -r rm -rf"
            .format(number + 1))
