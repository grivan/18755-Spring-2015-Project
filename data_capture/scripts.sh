#Script to capture Network Traffic, specifically length of the network packets being sent
sudo tcpdump | sed -n -e 's/.*length//p' | grep "<Protocol, UDP for P2P/Video for example>"

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

#Script to capture Disk IO, each second for five thousand seconds
sudo iotop -C 1 6000 -k -p 74339 -o | grep --line-buffered "<Application Name>"

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