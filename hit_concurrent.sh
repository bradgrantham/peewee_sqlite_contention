MB=25
SLEEP=.4

seq 1 100 | while read i
    do
        curl http://127.0.0.1:5050/dumb/$MB & > /dev/null
        curl http://127.0.0.1:5050/dumb/$MB & > /dev/null
        curl http://127.0.0.1:5050/dumb/$MB & > /dev/null
        curl http://127.0.0.1:5050/dumb/$MB & > /dev/null
        sleep $SLEEP
    done
