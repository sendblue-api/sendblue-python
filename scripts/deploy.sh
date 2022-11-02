#!/bin/bash

rm -rf ./dist
./scripts/build.sh

twine upload dist/*      
