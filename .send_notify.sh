#!/usr/bin/env bash
set -e
MSG=$(cat .notify_msg.txt)
./notify "$MSG"
