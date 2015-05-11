#Script to capture CPU usage per process
interval=60                         # reports per minute (max of 60)
timelimit=6000                      # how long to run, in seconds
mydate=`date "+%H:%M:%S"`           # the timestamp
freq=$((60/$interval))              # for sleep function
while [ "$SECONDS" -le "$timelimit" ] ; do
  ps -p$1 -opid -opcpu -ocomm -c | grep $1 | sed "s/^/$mydate /" | awk '{print $3}'
  sleep $freq
  mydate=`date "+%H:%M:%S"`
done
