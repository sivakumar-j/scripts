#!/bin/bash
set -vx


MAIL_ADDRESS=user@gmail.com

source /config/check_wasnd_jvm_run.config

v_host=$HOSTNAME
v_send_mail_p=0
v_mail_content-"Below List of JVM's are down in $v_host \n"
v_mail_content="${v_mail_content}*************\n"

for i in 'cat /prod/batch/scripts/country_list_control'
do
	if [ $v_alert_when_running ="N"]; #checks when not running
	then
		if ! pgrep -f "appname${i, ,}_server${v_server}" > /dev/null
		then
			v_send_mail_p=1
			v_mail_content="${v_mail_content}appname${i}_server${v_server} \n"
		fi

	elif [ $v_alert_when_running = "Y" ]; #checks when running
	then

		if pgrep -f "appname${i, ,}_server${v_server)" > /dev/null
		then
			v_send_mail p=1
			v_mail_content="${v_mail_content}appname${i}_server${v_server}\n"
		fi
         fi
done

MAIL SUBJECT="List of JVM's down in server ${v_host}"

if [ $v_send_mail_p -gt 0 ]
then

	echo -e "${v_mail_content}" | mail -s "$MAIL SUBJECT" "$MAIL ADDRESS"

fi

