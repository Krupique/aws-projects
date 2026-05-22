# Local execution

**Dev mode**
* `flask run`


**Production mode (with threads)**
* `gunicorn -w 4 app:app`


# Deploy on AWS

1. Select the EC2 service
   * Create an instance on EC2
   * Select the image (Amazon Linux)
   * Choose the architecture (64 bits x86)
   * Select or create key pair keys (.pem if you use Linux or Mac and .ppk if you use Windows)
   * On network settings you are going to create a new security group (save the name launch-wizard-1)
   * Select Allow SSH traffic from, Allow HTTPs traffic from the internet and Allow HTTP traffic from the internet
   * Then you click in Lauch Instance;

2. On the main page of EC2 you can see all instances that are running and when we select one instance, AWS shows some information about the instance that you've created:
   * Public DNS: It's the address you'll use to access your machine;
   * P.S.: If you want to configure a custom address, you'll have to use another service to configure custom DNS;
   * Then, select the instance and click in connect;

3. The simple way to connect on terminal is by EC2 Instant Connect, using a public IP and then connect

4. If you want to connect in the remote way, you need to select SSH client and follow the steps that is explained on the Connect screen;
   1. If you use windows, follow this [tutorial](https://www.youtube.com/watch?v=zDA9uEem2t0&list=PLBQYiqz5cudXETy8CWjl-RrVOe1RFdY4b&index=4) to understand how to connect on EC2 terminal via putty

5. In order to connect the Filezilla, you must to download the app Filezilla. So you open the app, then click on open the site manager and put the follow settings:
    * Protocol: SFTP - SSH File Transfer Protocol;
    * Host: Select the public DNS;
    * Logon type: Key File;
    * User: ec2-user;
    * Select your keyfile;
    * Save and connect;

6. Transfer the files from local to cloud using Filezilla;

7. Download and install the miniconda on AWS EC2 instance and all dependencies:
   * wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   * bash Miniconda3-latest-Linux-x86_64.sh
   * sudo yum install gcc
   * pip install -r requirements.txt

8. Running: gunicorn --bind 0.0.0.0:8000 app:app
   * It's missing something.
   * By default, AWS leaves the port 8000 closed, so we've got to allow this on the Firewall;
     * P.S: There are some opened ports by default: 22 (SSH), 80 (HTTP) and 443 (HTTPS). We can confirm that by going to the AWS EC2 panel on security tab;
   * AWS calls Firewall as Security Groups;
   * When you click in the security group name, you'll be taken to Security Group page;
   * In this page, you can add a new rule to allow the conections to the 8000 port;
     * Add Custom TCP, 8000 and allow connections from 0.0.0.0/0 (internet address);
   * Now It's possible to run with the terminal opened;

9. Now we want to leave the service running even without the terminal opened. So we need to create a script that runs the gunicorn in background:
   * Execute this command: sudo nano /etc/systemd/system/gunicorn.service
   * Paste the code below:
```bash
[Unit]
Description=Gunicorn instance to serve application
After=network.target

[Service]
User=ec2-user
Group=ec2-user
WorkingDirectory=/home/ec2-user/prd_version_cloud
Environment="PATH=/home/ec2-user/miniconda3/bin"
ExecStart=/home/ec2-user/miniconda3/bin/gunicorn --workers 3 --bind 0.0.0.0:8000 app:app
ExecReload=/bin/kill -s HUP $MAINPID
KillMode=mixed
TimeoutStopSec=5
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```
   * `Ctrl X` -> `Y` and `Enter` to save the file;
   * `cat /etc/systemd/system/gunicorn.service` if you want to check wheter the script was created;

* In order to finish, we need to run these commands to start the script:

```bash
sudo systemctl daemon-reload
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
sudo systemctl status gunicorn
sudo systemctl restart gunicorn
sudo systemctl stop gunicorn
journalctl -u gunicorn
```
