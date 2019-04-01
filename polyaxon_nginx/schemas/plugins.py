# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from polyaxon_nginx import settings
from polyaxon_nginx.schemas.base import get_config

OPTIONS = """
location ~ /tensorboard/proxy/([-_.:\w]+)/(.*) {{
    resolver {dns_prefix}.svc.{cluster_dns} valid=5s;
    rewrite_log on;
    rewrite ^/tensorboard/proxy/([-_.:\w]+)/(.*) /$2 break;
    proxy_pass http://$1;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Origin "";
}}

location ~ /notebook/proxy/([-_.:\w]+)/(.*) {{
    resolver {dns_prefix}.svc.{cluster_dns} valid=5s;
    rewrite_log on;
    rewrite ^/notebook/proxy/([-_.:\w]+)/(.*) /notebook/proxy/$1/$2 break;
    proxy_pass http://$1;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Origin "";
}}
"""  # noqa


def get_plugins_location_config():
    if settings.DNS_PREFIX:
        dns_prefix = settings.DNS_PREFIX
    else:
        dns_prefix = '{}.kube-system'.format(settings.DNS_BACKEND)
    return get_config(options=OPTIONS,
                      indent=0,
                      dns_prefix=dns_prefix,
                      cluster_dns=settings.CUSTOM_CLUSTER_DNS)
