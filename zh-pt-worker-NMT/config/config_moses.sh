#!/bin/bash

BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && dirname `pwd` )"

export MODELS_DIR=$BASEDIR/models/zh-pt

# comment these two lines out if you do not need a recaser
# 如果不需要recaser可以使用#号注释掉

#export RECASER_PORT=2001
#export RECASER_INI=$MODELS_DIR/recaser.moses.ini

export TRANSL_PORT=2006
export TRANSL_INI=$MODELS_DIR/moses.ini
