#!/bin/bash

BASE_DIR="roles"

for dir in "$BASE_DIR"/*; do
    if [ -d "$dir" ]; then
        if [ -d "$dir/files" ]; then
            mkdir -p "$dir/files/common"
            find "$dir/files" -mindepth 1 -maxdepth 1 -not -name 'common' -exec mv -t "$dir/files/common" {} +
        fi
    fi
done
