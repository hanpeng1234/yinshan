#!/bin/bash
while [ ! -d "/etc/alternatives/jre/lib/ext" ] ;
	do
		sleep 1
	done
set -x -e
aws s3 cp s3://rupiahplus-configs/postgresql-42.2.9.jar ~/postgresql.jar
sudo cp ~/postgresql.jar /etc/alternatives/jre/lib/ext/
exit 0

