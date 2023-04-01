#!/usr/bin/env python3
from subprocess import Popen, PIPE

with open('sudo_pwd.txt', 'r') as f:
    sudo_pwd = f.readline()


# passing sudo password directly (from a security perspective not a good idea!)
# https://stackoverflow.com/a/13045700/5899585
def restart_raspotify_service():
    command = 'service raspotify restart'.split()
    p = Popen(['sudo', '-S'] + command, stdin=PIPE, stderr=PIPE,
          universal_newlines=True)
    sudo_prompt = p.communicate(sudo_pwd+ '\n')[1]



if __name__ == '__main__':
    restart_raspotify_service()
