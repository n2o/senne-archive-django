#!/bin/sh

tar --exclude='./.*' \
    --exclude='tarball_without_media.sh' \
    --exclude='./media' \
    --exclude='./*.bak' \
    --exclude='./*.idea' \
    --exclude='./*.circleci' \
    --exclude='./*/__pycache__' \
    --exclude='*.pyc' \
    --exclude='*.scss' \
    --exclude='*.less' \
    -zcvf senne-deploy.tgz .
