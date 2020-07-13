ps -ef | grep "python3 main.py" | grep -v grep | awk '{print $2}' | xargs kill
