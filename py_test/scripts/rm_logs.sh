#!/bin/bash

###############################################################################
# author: BrentHuang (guang11cheng@qq.com)
###############################################################################

# 删除所有的日志文件

SCRIPT_PATH=$(cd `dirname $0`; pwd)

find ${SCRIPT_PATH}/.. -name "my_app.lock" | xargs rm -rf
find ${SCRIPT_PATH}/.. -name "my_app.log*" | xargs rm -rf
