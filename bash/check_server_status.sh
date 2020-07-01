#set -vx
#!/bin/bash

check_server_status()
{
 printf "IP inside fun is $1 \n"
 ping -c 1 $1 > /dev/null
 [ $? -eq 0 ] && echo Server with IP $i is up
}

printf "Line One \n"


for i in 3.133.12.{229..230}  #need to change according to CIDAR value
do
printf "IP is $i \n"
check_server_status $i & disown
done
exit
