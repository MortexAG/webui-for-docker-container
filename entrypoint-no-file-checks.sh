#!/bin/sh

# Check if /data is empty
if [ -z "$(ls -A /data)" ]; then
   echo "/data is empty. Copying default files from /data_original..."
   cp -a /data_original/. /data/
else
   echo "/data is not empty. Proceeding with existing files..."
fi

# Execute the main container command
exec "$@"
