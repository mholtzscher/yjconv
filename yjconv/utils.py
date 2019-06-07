"""
Utilities for parsing yaml and json
"""
import json
import yaml


def parse_as_yaml(data):
    """Attempt to parse data as yaml."""
    return yaml.load(data, Loader=yaml.FullLoader)


def parse_as_json(data):
    """Attempt to parse data as json."""
    return json.loads(data)
