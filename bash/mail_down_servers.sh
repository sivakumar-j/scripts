set -vx
#!/bin/bash

for i in $@
do
	ping -c 1 $i > /dev/null &&
       if [ $? -ne 0 ] ; then
	echo ping  failed for  server $i
        mail -s "host $i is down" emailid@gmail.com
       fi
done
exit
