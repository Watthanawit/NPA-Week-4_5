import pexpect

prompt = 'R2#'
ip = '172.31.173.5'
username = 'admin'
password = 'cisco'
command = 'sh ip int br'

child = pexpect.spawn('telnet ' + ip)
child.expect('Username')
child.sendline(username)
child.expect('Password')
child.sendline(password)
child.expect(prompt)
child.sendline(command)
child.expect(prompt)
result = child.before
print(result)
#child.sendline('exit')
child.close()
