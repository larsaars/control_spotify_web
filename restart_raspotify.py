import os

with open('sudo_pwd.txt', 'r') as f:
    sudo_pwd = f.readline()

restart_command = 'sudo systemctl restart raspotify.service'


# passing sudo password directly (from a security perspective not a good idea!)
# https://stackoverflow.com/a/13045700/5899585
def restart_rapotify_service():
    os.system('echo %s | sudo -S %s' % (sudo_pwd, restart_command))


restart_rapotify_service()