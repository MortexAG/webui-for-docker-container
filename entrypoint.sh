#!/bin/sh

# Loop through each item in /data_original
for item in /data_original/*; do
    itemname=$(basename "$item")
    # Check if the item is a directory
    if [ -d "$item" ]; then
        # Copy the directory if it doesn't exist in /data
        if [ ! -d "/data/$itemname" ]; then
            echo "Copying missing directory: $itemname"
            cp -r "$item" "/data/$itemname"
        fi
    else
        # If the item is a file, check if it exists in /data and copy if it doesn't
        if [ ! -f "/data/$itemname" ]; then
            echo "Copying missing file: $itemname"
            cp "$item" "/data/$itemname"
        fi
    fi
done

echo "Proceeding with existing or copied files and directories..."

# Execute the main container command
exec "$@"
