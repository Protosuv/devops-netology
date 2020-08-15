#!/usr/bin/env bash

COUNT=$1
PORT=$2
IP_ADDR=(192.168.0.1 173.194.222.113 87.250.250.242)
LOG_FILE=$HOME/curl_log.log
FULLDATE="`date +%Y_%m_%d_%X`"
for ADDR in ${IP_ADDR[@]}
do
    cnt=1
    while [ "$cnt" -le "$COUNT" ]
    do
        echo -e "IP address service: $ADDR" >> $LOG_FILE
        curl -vs http://$ADDR:$PORT 1>/dev/null 2>/dev/null
#        CURL_RESULT=$?
        if (($? != 0))
            then
            echo -e "$FULLDATE: Service on $ADDR:$PORT is unavaliable! Curl status = $?" >> $LOG_FILE
            else
            echo -e "$FULLDATE: Service on $ADDR:$PORT is OK! Curl status = $?" >> $LOG_FILE
        fi
    ((cnt++))
    done
done
exit 0
