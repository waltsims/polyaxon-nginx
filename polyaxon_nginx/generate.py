# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from polyaxon_nginx.schemas.polyaxon import get_polyaxon_config


def write_to_conf_file(name, content, path=None):
    with open('{}/{}.conf'.format(path or '.', name), 'w') as f:
        f.write(content)


def generate_nginx_conf(path=None):
    write_to_conf_file('polyaxon', get_polyaxon_config(), path)
    write_to_conf_file('nginx', get_polyaxon_config(), path)
