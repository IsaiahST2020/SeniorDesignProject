#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from octorest import OctoRest

client = True

def make_client():
    global client
    """
    Creates and returns an instance of the OctoRest client.
    Parameters:
        url - the url to the octoprint server
        apikey - the apikey from the octoprint server found in settings
    """
    url = "http://octopi.local"
    apikey = "21BA190BCA9E49289245D9D0B36C9CE1"
    try:
        client = OctoRest(url=url, apikey=apikey)
    except:
        print("Warning -- connection to OctoprintAPI could not be established...")

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'milestone3.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    make_client()
    main()
