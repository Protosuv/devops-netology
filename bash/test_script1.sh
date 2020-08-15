#!/usr/bin/env bash

while ((1==1))
do
        curl -vs https://localhost:4757 1>/dev/null 2>/dev/null
    if (($? != 0))
    then
           date >> curl.log
        else
        echo -e "Service is OK"
        exit 0
fi
