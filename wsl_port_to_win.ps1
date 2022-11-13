# get wsl ip
$ip_info = bash.exe -c "ifconfig eth0 | grep 'inet '"
$ip_ok = $ip_info -match '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
$ip = $Matches[0]
echo "now wsl ip: $ip"
# port forwarding
netsh interface portproxy add v4tov4 listenport=2222 listenaddress=* connectport=2222 connectaddress=$ip
# show all
netsh interface portproxy show all