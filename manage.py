#!/usr/bin/env python
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
import sys
import time
from rich.progress import track

def main():
    print("this is hyperdash test | version 0")
    print("Everythings is working well  \n  Please Wait.......")

    for i in track(range(10), description="Precessing..."):
        print(f"working {i}")
        time.sleep(0.5)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
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
    main()
