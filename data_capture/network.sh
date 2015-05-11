 #Script to capture Network Traffic, specifically length of the network packets being sent
sudo tcpdump | sed -n -e 's/.*length//p' | grep "<Protocol, UDP for P2P/Video for example>"
