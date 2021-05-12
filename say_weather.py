import subprocess


# execute cmd in unix
def execute_unix(input_command: str):
    p = subprocess.Popen(input_command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    return output


# say sth via tts
def say(inp: str, volume):
    cmd = 'espeak -ven+f3 -k5 -s150 -a %s --punct="<characters>" "%s" 2 >> /dev/null' % (str(volume), inp)
    execute_unix(cmd)


