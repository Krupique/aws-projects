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
   * 
