#!/bin/sh

cd /kannji/api-server/

# start hug dev server with file from argument
hug -f $@