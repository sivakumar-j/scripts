set -vx
#!/bin/bash

LOG=/tmp/logtestlog.log
seconds=300

for i in $@; do
 echo "$i-UP!" > $LOG.$i
done

while true; do
 for i in $@; do
  ping -c 1 $i > /dev/null
  if [ $? -ne 0 ]; then
	STATUS=$(cat  $LOG.$i)
	if [ $STATUS  == "$i-DOWN!" ]; then
		echo "IF2 $date Host $i is down"
	fi
  	echo  "$i-DOWN!" > $LOG.$i
  else
	STATUS=$(cat  $LOG.$i)
	if [ $STATUS  == "$i-UP!" ]; then
		echo "IF3 $date Host $i is UP"
	fi
  	echo  "$i-UP!" > $LOG.$i
  fi
 done
sleep $seconds
done

exit
