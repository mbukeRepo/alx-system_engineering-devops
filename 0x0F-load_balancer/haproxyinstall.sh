apt-get install -y software-properties-common
add-apt-repository -y ppa:vbernat/haproxy-1.8
apt-get update
apt-get install -y haproxy=1.8.\*
