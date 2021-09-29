#!/bin/bash
set -vx
date

v_running= `pgrep -c night_batch_deamon.sh -U fid_one`

if [ $v running -ge 1 ];
then
	echo
	"Error:  night_batch_deamon.sh already running. Cannot Run again"
	exit 9
fi

nohup /prod/app_one/batch/jobs/scripts/night_batch_deamon.sh >> /prod/app_one/batch/jobs/log/night_batch_deamon.log

sleep 2s

v_post run= `pgrep -c night_batch_deamon.sh -U fid_one`

if [ $v_post_run_ -ge 1 ];
then
	echo "Success: night_batch_deamon.sh script is started"
else
	echo "Error: NOT started night_batch_deamon.sh script.Please check"
fi

date
