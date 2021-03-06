#!/bin/bash

###############################################################################
# author: BrentHuang (guang11cheng@qq.com)
###############################################################################

SCRIPT_PATH=$(cd `dirname $0`; pwd)

LOG_DIR=${SCRIPT_PATH}/../logs/

if [ $# -gt 0 ]; then
    find ${LOG_DIR} -name "*.error.log" | xargs tail -F
else
    find ${LOG_DIR} -name "*.error.log" | xargs more
fi
