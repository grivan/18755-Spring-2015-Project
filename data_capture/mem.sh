#Script to capture RAM/Memory
interval=60                         # reports per minute (max of 60)
timelimit=6000                      # how long to run, in seconds
mydate=`date "+%H:%M:%S"`           # the timestamp
freq=$((60/$interval))              # for sleep function
while [ "$SECONDS" -le "$timelimit" ] ; do
  top -l 1| grep "<Process ID>" | awk '{print "MEM="$9}'
  sleep $freq
  mydate=`date "+%H:%M:%S"`
done
