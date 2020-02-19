#!/bin/sh

s3fs sandbox ~/development/devnet-create/snapshots/sandbox -o passwd_file=${HOME}/.passwd-s3fs -o url=http://minio:9000 -o use_path_request_style