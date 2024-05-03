#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers
"""
from fabric.api import env, local, put, run, runs_once
from datetime import datetime
import os.path

env.hosts = ['54.90.33.112', '23.23.75.134']


@runs_once
def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static.
    """
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        now = datetime.now()
        file_format = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second)
        local("tar -cvzf {} web_static".format(file_format))
        return file_format
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    """
    if not exists(archive_path):
        return False
    file_name = archive_path.split('/')[-1]
    folder_name = file_name.replace('.tgz', '')
    put(archive_path, '/tmp/')
    run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(file_name, folder_name))
    run('rm /tmp/{}'.format(file_name))
    run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(folder_name, folder_name))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(folder_name))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(folder_name))
    return True


def deploy():
    """
    Creates and distributes an archive to the web servers.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
