#!/usr/bin/python3
#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers.
"""
from fabric.context_managers import cd, hide,\
        settings, show, path, prefix, lcd, quiet, warn_only,\
        remote_tunnel, shell_env
from fabric.decorators import hosts, roles,\
        runs_once, with_settings, task, serial, parallel
from fabric.operations import require, prompt,\
        put, get, run, sudo, local, reboot, open_shell
from fabric.state import env, output
from fabric.utils import abort, warn, puts, fastprint
from fabric.tasks import execute
from datetime import datetime
import os

env.hosts = ['54.90.33.112', '23.23.75.134']
env.user = "ubuntu"


def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder.

    Returns:
        The path to the generated archive.
    """
    try:
        my_time = datetime.now().strftime('%Y%m%d%H%M%S')
        local("mkdir -p versions")
        my_file = 'versions/web_static_' + my_time + '.tgz'
        local('tar -vzcf {} web_static'.format(my_file))
        return (my_file)
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Distribute an archive to web servers.

    Args:
        archive_path (str): The path of the archive to distribute.

    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    path_existence = os.path.exists(archive_path)
    if path_existence is False:
        return False
    try:
        path_split = archive_path.replace('/', ' ').replace('.', ' ').split()
        just_directory = path_split[0]
        no_tgz_name = path_split[1]
        full_filename = path_split[1] + '.' + path_split[2]
        folder = '/data/web_static/releases/{}/'.format(no_tgz_name)
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(folder))
        run('tar -xzf /tmp/{} -C {}/'.format(full_filename, folder))
        run('rm /tmp/{}'.format(full_filename))
        run('mv {}/web_static/* {}'.format(folder, folder))
        run('rm -rf {}/web_static'.format(folder))
        current = '/data/web_static/current'
        run('rm -rf {}'.format(current))
        run('ln -s {}/ {}'.format(folder, current))
        return True
    except Exception:
        return False


def deploy():
    """
    Create and distribute an archive to the web servers.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
