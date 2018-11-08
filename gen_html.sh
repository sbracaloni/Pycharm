#!/bin/bash -eux

pushd $(git rev-parse --show-toplevel)/doc
echo "GENERATE HTML FILES"
echo $(pwd)
rm -rf ./html
reveal-md setup.md --static ./html
ln -s ../images ./html/images

popd