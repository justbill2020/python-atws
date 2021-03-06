# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
import click
from .wrapper import connect
from .helpers import create_atvar_module
from .monkeypatch.duckpunch import BLACKLISTED_TYPES, get_api_types

@click.command()
@click.argument('target_path')
@click.option('--username', 
              default=os.environ.get('AUTOTASK_API_USERNAME', None), 
              help='your Autotask username')
@click.option('--password',
              default=os.environ.get('AUTOTASK_API_PASSWORD', None), 
              help='your Autotask password')
@click.option('--url',
              default=os.environ.get('AUTOTASK_API_URL', None), 
              help='your Autotask webservices URL (wsdl file)')
@click.option('--entities',
              default=list(), 
              help='Space delimited entity types for inclusion')
def main(target_path, username, password, url, entities):
    
    at = connect(url=url,
                      username=username,
                      password=password)
    
    if not entities:
        entities = get_api_types(at.client, BLACKLISTED_TYPES)
    
    create_atvar_module(at, entities, target_path)


if __name__ == "__main__":
    main()