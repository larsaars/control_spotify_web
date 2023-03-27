; inspired by : https://github.com/iver56/clap-detection

<CsoundSynthesizer>
<CsOptions>
-iadc
--nosound
</CsOptions>
<CsInstruments>

sr = 44100
ksmps = 32
nchnls = 1
0dbfs  = 1

pyinit

instr 1

pyruni {{

# import and add path
import os, sys, traceback
sys.path.append(os.getcwd())
print(sys.version)

from spotify_tools import *

# the time of the last clap (to remember)
before = 0
sumOfClaps = 1

# gets called when clap has been detected
def clap_detected(now):
    # set global variable is accessed
    global before, sumOfClaps
    # calculate the time difference from the last clap
    diff = now - before

    print('clap', diff)

    # if the difference is less than 0.4 it is a fast double clap and given code will be executed
    # in this case spotify play / pause
    if diff < CLAP_TIME_DIFF:
        # the sum of claps is plus one
        sumOfClaps += 1
        # if two claps, play pause
        if sumOfClaps == 2:
            # check boolean, if is playing, enable playback, if not, disable playback
            # wrap in try catch
            try:
                if is_playing():
                    spotify.pause_playback()
                else:
                    spotify.start_playback()
            except Exception:
                try_ensure_device()
                traceback.print_exc()

                sleep(3)

                try:
                    spotify.start_playback()
                except:
                    pass
        elif sumOfClaps == 3:
            spotify.next_track()
    else:
        sumOfClaps = 1

    # set the before clap as now time
    before = now

}}

kLastRms init 0
kLastAttack init 0
iRmsDiffThreshold init .1

kTime times

aIn in

kRmsOrig rms aIn

kSmoothingFreq linseg 5, 1, 0.01 ;quicker smoothing to start with
kSmoothRms tonek kRmsOrig, kSmoothingFreq
kSmoothRms max kSmoothRms, 0.001

aNorm = 0.1 * aIn / a(kSmoothRms)

kRms rms aNorm
kRmsDiff = kRms - kLastRms

if (kRmsDiff > iRmsDiffThreshold && kTime - kLastAttack > 0.09) then
        kLastAttack times
        pycall "clap_detected", kLastAttack
endif

out aNorm
kLastRms = kRms

endin
</CsInstruments>
<CsScore>

i 1 0 500
e
</CsScore>
</CsoundSynthesizer>
