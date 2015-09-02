#! /usr/bin/env sh

sshpass -p "hsruser" ssh hsr-user@hsrb "arecord -d 6 out.wav"
sshpass -p "hsruser" scp hsr-user@hsrb:/home/hsr-user/out.wav `rospack find hsr_task_common`/out.wav
