[0;1;32m●[0m gunicorn.service - gunicorn daemon
   Loaded: loaded (/etc/systemd/system/gunicorn.service; disabled; vendor preset: enabled)
   Active: [0;1;32mactive (running)[0m since Wed 2020-03-11 22:19:00 UTC; 5s ago
 Main PID: 3203 (gunicorn)
    Tasks: 4 (limit: 1152)
   CGroup: /system.slice/gunicorn.service
           ├─3203 /home/ubuntu/cardsense/venv/bin/python3 /home/ubuntu/cardsense/venv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/cardsense/walloffame.sock walloffame.wsgi:application
           ├─3222 /home/ubuntu/cardsense/venv/bin/python3 /home/ubuntu/cardsense/venv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/cardsense/walloffame.sock walloffame.wsgi:application
           ├─3224 /home/ubuntu/cardsense/venv/bin/python3 /home/ubuntu/cardsense/venv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/cardsense/walloffame.sock walloffame.wsgi:application
           └─3225 /home/ubuntu/cardsense/venv/bin/python3 /home/ubuntu/cardsense/venv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/cardsense/walloffame.sock walloffame.wsgi:application

Mar 11 22:19:00 ip-172-31-26-236 systemd[1]: Started gunicorn daemon.
Mar 11 22:19:00 ip-172-31-26-236 gunicorn[3203]: [2020-03-11 22:19:00 +0000] [3203] [INFO] Starting gunicorn 20.0.4
Mar 11 22:19:00 ip-172-31-26-236 gunicorn[3203]: [2020-03-11 22:19:00 +0000] [3203] [INFO] Listening at: unix:/home/ubuntu/cardsense/walloffame.sock (3203)
Mar 11 22:19:00 ip-172-31-26-236 gunicorn[3203]: [2020-03-11 22:19:00 +0000] [3203] [INFO] Using worker: sync
Mar 11 22:19:00 ip-172-31-26-236 gunicorn[3203]: [2020-03-11 22:19:00 +0000] [3222] [INFO] Booting worker with pid: 3222
Mar 11 22:19:01 ip-172-31-26-236 gunicorn[3203]: [2020-03-11 22:19:01 +0000] [3224] [INFO] Booting worker with pid: 3224
Mar 11 22:19:01 ip-172-31-26-236 gunicorn[3203]: [2020-03-11 22:19:01 +0000] [3225] [INFO] Booting worker with pid: 3225
