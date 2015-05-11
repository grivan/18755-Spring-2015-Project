#Script to capture Disk IO, each second for five thousand seconds
sudo iotop -C 1 6000 -k -p 74339 -o | grep --line-buffered "<Application Name>"
