#!/bin/bash
pyinstaller --onefile main.py --osx-bundle-identifier={{cookiecutter.reverse_domain_id}} --name={{cookiecutter.project_name}}