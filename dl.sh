#!/bin/bash

BASEURL=$(printf "http://www.ikyu.com/%08d/review/" $1)
FILENAME=$(printf "%08d.html" $1)

echo $BASEURL
curl $BASEURL > $FILENAME

sleep 9

for i in $(seq 2 $2); do
    PARAM=$(printf "?pn=%d" $i)
    URL="${BASEURL}${PARAM}"
    FILENAME=$(printf "%08d-%d.html" $1 $i)
    curl $URL > $FILENAME
    sleep 9
done

