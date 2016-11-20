#! /bin/bash
#
# deploy.sh
# Copyright (C) 2016 dhilipsiva <dhilipsiva@gmail.com>
#
# Distributed under terms of the MIT license.
#

echo "Deploying to GemFury"
bumpversion patch
git push origin
git push origin --tags
python setup.py sdist
python setup.py bdist_wheel
twine upload dist/*
