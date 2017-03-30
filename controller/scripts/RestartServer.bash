ZhPID=$(cat /home/luyi/zh-pt-worker-v1/PID)
PtPID=$(cat /home/luyi/pt-zh-worker-v1/PID)
RPID=$(cat /home/luyi/controller/appserver/PID)
echo "Start to kill process"
kill $ZhPID
kill $PtPID
kill $RPID
echo "Finished kill server"
echo "Start to restart the server"
/home/luyi/controller/scripts/run_ruletranslate
/home/luyi/pt-zh-worker-v1/scripts/run_worker
/home/luyi/zh-pt-worker-v1/scripts/run_worker
echo "Restarted"
