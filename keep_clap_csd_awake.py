"""
I had the problem that the command csound clap.csd exits after 500s,
so i wrote this script so that it runs without pause
"""
import subprocess


def main():
    # infinite loop starting csound process and sleeping again
    while True:
        print('restarting clap.csd')

        # create process, and wait for it
        process = subprocess.Popen('csound clap.csd', shell=True, stdout=subprocess.PIPE)
        process.wait()


if __name__ == '__main__':
    main()
