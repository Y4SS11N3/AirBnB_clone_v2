#!/usr/bin/python3
"""
Fabric script that manages the archives of web static deployments
"""
from fabric.api import *
from os import path
from datetime import datetime

env.hosts = ['54.90.33.112', '23.23.75.134']

def do_pack():
    """Generates a .tgz archive from the contents of the 'web_static' folder"""
    try:
        date_time = datetime.now().strftime("%Y%m%d%H%M%S")
        if not path.exists("versions"):
            local("mkdir versions")
        archive_path = "versions/web_static_{}.tgz".format(date_time)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        return None

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not path.exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        file_without_ext = file_name.split(".")[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(file_without_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file_name, file_without_ext))
        run("rm /tmp/{}".format(file_name))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(file_without_ext, file_without_ext))
        run("rm -rf /data/web_static/releases/{}/web_static".format(file_without_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(file_without_ext))
        return True
    except Exception as e:
        return False

def deploy():
    """Creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
    if number == 0:
        number = 1
    local("ls -t versions/web_static_*.tgz | tail -n +{} | xargs rm -rf".format(number + 1))
    run("ls -t /data/web_static/releases/ | grep 'web_static_' | tail -n +{} | xargs -I {{}} rm -rf /data/web_static/releases/{{}}".format(number + 1))
