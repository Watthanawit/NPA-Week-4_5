import paramiko
import getpass
import time

username = 'admin'
password = 'cisco'

device_ip = ["172.31.173.4", "172.31.173.1"]

for ip in device_ip:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip, username=username, password=password, look_for_keys=False, allow_agent=False)

    with client.invoke_shell() as ssh:
        print("Connected to {} ...".format(ip))

        ssh.send("teminal length 0\n")
        time.sleep(1)
        #result = ssh.recv(1000).decode('ascii')
        #print(result)

        ssh.send("sh ip int br\n")
        time.sleep(1)
        result = ssh.recv(10000).decode('ascii')
        print(result)

