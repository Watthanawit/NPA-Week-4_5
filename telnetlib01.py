import getpass
import telnetlib
import time

host = "172.31.173.5"
user = input("Enter username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(host, 23, 5)

tn.read_until(b"Username:")
tn.write(user.encode('ascii') + b"\n")
time.sleep(1)

tn.read_until(b"Password:")
tn.write(password.encode('ascii') + b"\n")
time.sleep(1)

tn.write(b"show ip int br\n")
time.sleep(2)
tn.write(b"exit\n")
time.sleep(1)

output = tn.read_all()
print(output.decode('ascii'))

tn.close()
