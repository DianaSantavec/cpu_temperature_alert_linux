#!/bin/bash

#get highest temperature of a core
sensors -j | sed -e 's/-//g' > sed -e 's/ //g' > sed -e 's/_//g' > test.json
temperature= cat test.json | jq .coretempisa0000.Packageid0.temp1input

critical_temperature=94
#compare temperature with limit
if [ $temperature > $critical_temperature ]
then
    notify-send Test "hello world"
else
    notify-send Test "hellllo woooorld"
fi