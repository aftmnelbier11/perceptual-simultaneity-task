# Perceptual Simultaneity Task
###################################################################################
# Copyright (c) 2023 Afton M. Nelson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
###################################################################################

import os
import sys
from psychopy import data, visual, core, event, gui, logging
from psychopy.constants import (NOT_STARTED, FINISHED)
import random

# Set Directory
thisDir = os.path.dirname(os.path.abspath(__file__))  # sets path to same path as script file location
os.chdir(thisDir)  # changes working directory to the path thisDir

# Setup GUI
myDlg = gui.Dlg(title='Perceptual Simultaneity Task')
myDlg.addField('ID', )
myDlg.addField('Diagnosis', choices=["TD", "ASD"])  # TD = typically-developed ; ASD = Autism Spectrum Disorder
myDlg.addField('Age', )
myDlg.addField('Gender', choices=["M", "F", "NB"])  # M = male ; F = female; NB = non-binary
myDlg.addField('Handedness', choices=["R", "L", "B"])  # L = left ; R = right ; B = both
ok_data = myDlg.show()  # show dialog and wait for OK or Cancel
if myDlg.OK:  # if ok_data then save info as subject or else cancel
    subject = myDlg.data
else:
    print('user cancelled')

# Write session info in the dictionary 'ExpInfo'
expName = 'Perceptual Simultaneity Task'
expName2 = 'PIPS'  # abbreviation of full experiment name for file label - full exp name within file
psychopyVersion = '2020.2.5'
sessionDate = data.getDateStr()  # gives a timestamp

expInfo = {}
expInfo['date'] = sessionDate
expInfo['expName'] = expName
expInfo['PsychoPyVersion'] = psychopyVersion
expInfo['subjectID'] = subject[0:5]

# Create path to export data files
fileName = thisDir + os.sep + u'data/%s_%s_%s_%s' % (expName2, subject[0], subject[1], expInfo['date'])

# Define the expHandler
thisExp = data.ExperimentHandler(name=expName, version=psychopyVersion,
                                 originPath='C:/Users/Admin/Desktop/Afton/NON_new/',
                                 savePickle=False, saveWideText=True,
                                 dataFileName=fileName)

# moved out of the expHandler, as not to record subject info for every trial
thisExp.addData('ExpInfo', expInfo)
thisExp.nextEntry()

# save a log file of experiment action execution (logging.EXP)
logFile = logging.LogFile(fileName + '.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
# Create methods (luminance (1-5), stimulus onsets (sync or async)) for stimuli selection and initialization

# list of luminance increments (padded by black [0] and brightest grey [127.5])
ll = [0] * 12
ll.append(25.5)
ll.append(51.0)
ll.append(76.5)
ll.append(102.0)
ll.append(127.5)
trailing = [127.5] * 12
ll.extend(trailing)

print(ll)

# create index for conditions
positions_stimuliList = []

for digit in range(1, 27):
    positions_stimuliList.append(digit)

# create a list of dictionary of condition specs (SOA, bar appearance, luminance setting)
stimuliOnsetList = []
for stimulus in positions_stimuliList:
    if stimulus == 1:
        SOA = 0  # SOA condition
        L_R = 0  # 0 is simultaneous, -1 is L first, 1 is R first
        corrResp = 'c'  # correct response
        lumSeqL = ll[12:17]  # luminance settings for bar L
        lumSeqR = ll[12:17]  # luminance settings bar R
    elif stimulus == 2:
        SOA = 1
        L_R = -1
        corrResp = 'm'
        lumSeqL = ll[12:18]
        lumSeqR = ll[11:17]
    elif stimulus == 3:
        SOA = 2
        L_R = -1
        corrResp = 'm'
        lumSeqL = ll[12:19]
        lumSeqR = ll[10:17]
    elif stimulus == 4:
        SOA = 3
        L_R = -1
        corrResp = 'm'
        lumSeqL = ll[12:20]
        lumSeqR = ll[9:17]
    elif stimulus == 5:
        SOA = 4
        L_R = -1
        corrResp = 'm'
        lumSeqL = ll[12:21]
        lumSeqR = ll[8:17]
    elif stimulus == 6:
        SOA = 5
        L_R = -1
        corrResp = 'm'
        lumSeqL = ll[12:22]
        lumSeqR = ll[7:17]
    elif stimulus == 7:
        SOA = 6
        L_R = -1
        corrResp = 'm'
        lumSeqL = ll[12:23]
        lumSeqR = ll[6:17]
    elif stimulus == 8:
        SOA = 7
        L_R = -1
        corrResp = 'm'
        lumSeqL = ll[12:24]
        lumSeqR = ll[5:17]
    elif stimulus == 9:
        SOA = 8
        L_R = -1
        corrResp = 'm'
        lumSeqL = ll[12:25]
        lumSeqR = ll[4:17]
    elif stimulus == 10:
        SOA = 9
        L_R = -1
        corrResp = 'm'
        lumSeqL = ll[12:26]
        lumSeqR = ll[3:17]
    elif stimulus == 11:
        SOA = 10
        L_R = -1
        corrResp = 'm'
        lumSeqL = ll[12:27]
        lumSeqR = ll[2:17]
    elif stimulus == 12:
        SOA = 11
        L_R = -1
        corrResp = 'm'
        lumSeqL = ll[12:28]
        lumSeqR = ll[1:17]
    elif stimulus == 13:
        SOA = 12
        L_R = -1
        corrResp = 'm'
        lumSeqL = ll[12:29]
        lumSeqR = ll[0:17]
    if stimulus == 14:
        SOA = 0
        L_R = 0  # 0 is simultaneous, -1 is L first, 1 is R first
        corrResp = 'c'
        lumSeqL = ll[12:17]
        lumSeqR = ll[12:17]
    elif stimulus == 15:
        SOA = 1
        L_R = 1
        corrResp = 'm'
        lumSeqR = ll[12:18]
        lumSeqL = ll[11:17]
    elif stimulus == 16:
        SOA = 2
        L_R = 1
        corrResp = 'm'
        lumSeqR = ll[12:19]
        lumSeqL = ll[10:17]
    elif stimulus == 17:
        SOA = 3
        L_R = 1
        corrResp = 'm'
        lumSeqR = ll[12:20]
        lumSeqL = ll[9:17]
    elif stimulus == 18:
        SOA = 4
        L_R = 1
        corrResp = 'm'
        lumSeqR = ll[12:21]
        lumSeqL = ll[8:17]
    elif stimulus == 19:
        SOA = 5
        L_R = 1
        corrResp = 'm'
        lumSeqR = ll[12:22]
        lumSeqL = ll[7:17]
    elif stimulus == 20:
        SOA = 6
        L_R = 1
        corrResp = 'm'
        lumSeqR = ll[12:23]
        lumSeqL = ll[6:17]
    elif stimulus == 21:
        SOA = 7
        L_R = 1
        corrResp = 'm'
        lumSeqR = ll[12:24]
        lumSeqL = ll[5:17]
    elif stimulus == 22:
        SOA = 8
        L_R = 1
        corrResp = 'm'
        lumSeqR = ll[12:25]
        lumSeqL = ll[4:17]
    elif stimulus == 23:
        SOA = 9
        L_R = 1
        corrResp = 'm'
        lumSeqR = ll[12:26]
        lumSeqL = ll[3:17]
    elif stimulus == 24:
        SOA = 10
        L_R = 1
        corrResp = 'm'
        lumSeqR = ll[12:27]
        lumSeqL = ll[2:17]
    elif stimulus == 25:
        SOA = 11
        L_R = 1
        corrResp = 'm'
        lumSeqR = ll[12:28]
        lumSeqL = ll[1:17]
    elif stimulus == 26:
        SOA = 12
        L_R = 1
        corrResp = 'm'
        lumSeqR = ll[12:29]
        lumSeqL = ll[0:17]
    stimuliOnsetList.append({'SOA': SOA, 'L_R': L_R, 'corrResp': corrResp, 'lumSeqL': lumSeqL, 'lumSeqR': lumSeqR})

# trials randomly chosen for training block
trainingTrialsList = random.choices(stimuliOnsetList, k=10)


# -----------------------------------------------
# Methods for stimulus visualization

def insertInstructionText(text):
    return visual.TextStim(experiment_window, color='white',
                           text=text, units='norm', height=.1,
                           pos=[0, 0], anchorVert='center')


def insertText(text):
    return visual.TextStim(experiment_window, color='white',
                           text=text, units='norm', height=.1,
                           pos=[0, 0], anchorHoriz='center')


# ------------------------------------------
# Define methods to run the instructions
# included an insert because we have 2 instructions texts
def runInstructions(instructionsX):
    instructions_is_running = True
    while instructions_is_running:
        for i in range(0, sys.maxsize):
            instructionsX.draw()
            experiment_window.flip()
            event.clearEvents()
            kb_resp_instructions = event.waitKeys(keyList=['space'])
            if kb_resp_instructions:
                kb_resp_instructions = kb_resp_instructions[0]
                core.wait(0.001)  # make sure event was processed
                return


# ------------------------------------------
# Define methods to run the instructions
def runEndExp(endMessage):
    endExp_still_running = True
    while endExp_still_running:
        for i in range(0, sys.maxsize):
            endMessage.draw()
            experiment_window.flip()
            event.clearEvents()
            kb_resp_endExp = event.waitKeys(keyList=['space'])
            if kb_resp_endExp:
                kb_resp_endExp = kb_resp_endExp[0]
                core.wait(0.001)  # make sure event was processed
                return


# ------------------------------------------
# Define method to start/check/end the routine (instructions)
def initialize(i):
    for thisComponent in i:
        thisComponent.tStart = None
        thisComponent.tStop = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED


def finalize(i):
    for thisComponent in i:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            trial_still_running = True
            break  # at least one component of the trial has not finished running


def endTrial(i):
    for thisComponent in i:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)


# ------------------------------------------
# Method to escape the experiment
def checkForEscape():
    if event.getKeys(['escape']):
        print("QUIT EXPERIMENT")
        core.quit()


# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# Initialize experiment properties (expClock and the expWindow)
experiment_window = visual.Window(size=(800, 600), winType='pyglet', fullscr=True,
                                  screen=0, monitor='testMonitor',
                                  color="black", colorSpace='rgb')
experiment_window.mouseVisible = False
expClock = core.Clock()

frameTolerance = 0.001

# -------------------------------------------------------
# -------------------------------------------------------
# Initialize instructions stimuli
instructions1 = insertInstructionText(
    '- Fixieren Sie mit Ihren Augen während der gesamten Aufgabe das Kreuz in der Mitte.\n'
    '- Auf dem Bildschirm werden zwei Balken erscheinen.\n '
    '- Ihre Aufgabe ist festzustellen, ob die Balken gleichzeitig erscheinen. \n '
    '- Drücken Sie „c“ für „gleichzeitig“ oder „m“ für „nicht gleichzeitig“.')
instructions2 = insertInstructionText('Bitte antworten Sie so schnell und akkurat wie möglich. \n'
                                      'Drücken Sie die Leertaste, um den Übungsblockzu  beginnen. ')

instructionsClock = core.Clock()
instructionsTimer = core.CountdownTimer()
start_time = 0

instructions_still_running = True

instructionsClock.reset()
instructionsTimer.reset()
instructionsTimer.add(15)

instructionsComponents = [instructions1, instructions2]
initialize(instructionsComponents)

# Run instructions sequence
while instructions_still_running and instructionsTimer.getTime() > 0 - frameTolerance:
    start_time = instructionsClock.getTime()

    if start_time > 0 - frameTolerance and instructions1.status == NOT_STARTED:
        start_time = instructionsClock.getTime()
        instructions1.tStart = start_time
        runInstructions(instructions1)
        instructionEnd = instructionsClock.getTime()
        instructions1.tStop = instructions1.tStart + instructionEnd

        experiment_window.flip()
        nextComponent = instructions1.tStart + instructionEnd

    if instructionsClock.getTime() >= nextComponent - frameTolerance and instructions2.status == NOT_STARTED:
        instructions2_time = instructionsClock.getTime()
        instructions2.tStart = instructions2_time
        runInstructions(instructions2)
        instructionEnd = instructionsClock.getTime()
        instructions2.tStop = instructions2.tStart + instructionEnd

        experiment_window.flip()

    checkForEscape()

    experiment_window.flip()

    finalize(instructionsComponents)
    end_time = instructionsClock.getTime()
    instructions_still_running = False

endTrial(instructionsComponents)

# -------------------------------------------------------
# ------------------ PRACTICE BLOCK ---------------------
# -------------------------------------------------------
# Implement trialHandlers for blocks and trials; and initialize the practice block

practiceBlocks = data.TrialHandler(trialList=None, nReps=1)  # 1 block
thisExp.addLoop(practiceBlocks)

practiceBlockClock = core.Clock()

timeStim = []  # create list to store frame by frame information for each stimuli

for practiceBlock in practiceBlocks:
    practiceBlockClock.reset()
    practiceBlock_still_running = True

    while practiceBlock_still_running:
        block_start = practiceBlockClock.getTime()

        practiceTrials = data.TrialHandler(trialList=trainingTrialsList, nReps=1,
                                           method='random')  # list of 10 dictionaries of trial conditions for practice trials

        thisExp.addLoop(practiceTrials)

        practiceTrialClock = core.Clock()
        counter = 0  # counter of trials in block

        for practiceTrial in practiceTrials:
            counter = counter + 1
            print('Practice trial number:' + str(counter))
            print("SOA: " + str(practiceTrial['SOA']))
            print("L_R: " + str(practiceTrial['L_R']))
            print("corrResp: " + str(practiceTrial['corrResp']))

            fixationCross_coordinates = [(0, .1), (0, 0), (.1, 0), (-.1, 0), (0, 0), (0, -.1)]
            fixationCross = visual.ShapeStim(experiment_window, vertices=fixationCross_coordinates,
                                             units='cm', size=4, closeShape=False, lineWidth=2, pos=(0, 0))

            practiceTrialClock.reset()
            practiceTrial_still_running = True

            while practiceTrial_still_running:
                fixationCross.draw()
                experiment_window.flip()
                core.wait(0.5)
                fixationCross.draw()
                experiment_window.flip()

                nFrame = 0
                stimuliClock = core.Clock()
                stimuliClock.reset()

                for i, j in zip(practiceTrial['lumSeqL'], practiceTrial['lumSeqR']):
                    barL_coordinates = [(-5.75, -2.05), (-5.75, 2.05), (-5.35, 2.05), (-5.35, -2.05)]
                    barL = visual.ShapeStim(experiment_window, vertices=barL_coordinates, units='cm',
                                            size=1, closeShape=True, lineWidth=2, pos=(0, 0), lineColor=None,
                                            fillColor=i, fillColorSpace='rgb255')
                    barR_coordinates = [(5.35, -2.05), (5.35, 2.05), (5.75, 2.05), (5.75, -2.05)]
                    barR = visual.ShapeStim(experiment_window, vertices=barR_coordinates, units='cm',
                                            size=1, closeShape=True, lineWidth=2, pos=(0, 0), lineColor=None,
                                            fillColor=j, fillColorSpace='rgb255')

                    fixationCross.draw()
                    barL.draw()
                    barR.draw()
                    t = experiment_window.flip()
                    nFrame = nFrame + 1
                    timeStim.append((nFrame, t, practiceTrial['SOA'], len(practiceTrial['lumSeqL'])))

                event.clearEvents()
                kb_resp = event.waitKeys(keyList=['c', 'm'])  # m = anderes ; c = gleich
                kb_resp_RT = stimuliClock.getTime()
                if kb_resp:
                    print(kb_resp)
                    kb_resp = kb_resp[0]  # key not a list of them
                    core.wait(0.001)  # make sure event was processed
                    practiceTrial_still_running = False
                    end_time = practiceTrialClock.getTime()

                checkForEscape()
                experiment_window.flip()

            practiceTrials.addData('Practice Trial Number', counter)
            practiceTrials.addData('subjResp', kb_resp)
            practiceTrials.addData('respRT', kb_resp_RT)
            thisExp.nextEntry()

        if counter == 10:
            print('Practice block is done.')
            block_end = practiceBlockClock.getTime()
            blockMessage = insertText('Ende Übungsblock. Drücken Sie die Leertaste, um den Aufgabenblock zu beginnen.\n'
                                      'Drücken Sie „c“ für „gleichzeitig“ oder „m“ für „nicht gleichzeitig“.')
            blockMessage.draw()
            experiment_window.flip()
            core.wait(5)
            checkForEscape()
            event.clearEvents()
            kb_resp_continue = event.waitKeys(keyList=['space'])
            if kb_resp_continue:
                kb_resp_continue = kb_resp_continue[0]  # key not a list of them
                core.wait(0.001)  # make sure event was processed
                practiceBlock_still_running = False

# Write a csv of the frame info for each PRACTICE stimuli
# ---- includes frame number (frameN), time of the window flip based on a global clock (t),
# ---- the SOA condition (SOA), and the length of the luminance sequence (len(trial[lumSeq])

frameFile = thisDir + os.sep + u'data/frameseries/%s_%s_%s_%s_frameseries-pract.csv' % (
expName2, subject[0], subject[1], expInfo['date'])
f = open(frameFile, 'w')
for t in timeStim:
    line = ','.join(str(x) for x in t)
    f.write(line + '\n')
f.close()

# -------------------------------------------------------
# --------------- EXPERIMENTAL BLOCKS -------------------
# -------------------------------------------------------
# Implement trialHandlers for blocks, trials, and stimuli and initialize the experimental blocks

blocks = data.TrialHandler(trialList=None, nReps=5)  # 5 blocks
thisExp.addLoop(blocks)

blockClock = core.Clock()

blockCounter = 0

# moved on 09.08.2021
accuracyCounter = 0  # tracks response accuracy
expTrialCounter = 0  # tracks the total trial number -- counter just tracks the BLOCK trial number

for block in blocks:
    blockClock.reset()
    block_still_running = True

    while block_still_running:
        block_start = blockClock.getTime()
        blockCounter = blockCounter + 1
        print('Block Number' + str(blockCounter))

        trials = data.TrialHandler(trialList=stimuliOnsetList, nReps=2,
                                   method='random')  # list of 26 dictionaries (for each condition) repeated twice
        thisExp.addLoop(trials)

        trialClock = core.Clock()
        counter = 0  # tracks trials

        for trial in trials:
            expTrialCounter = expTrialCounter + 1
            counter = counter + 1
            print('trial number:' + str(counter))
            print("SOA: " + str(trial['SOA']))
            print("L_R: " + str(trial['L_R']))
            print("corrResp: " + str(trial['corrResp']))

            start_time = 0

            fixationCross_coordinates = [(0, .1), (0, 0), (.1, 0), (-.1, 0), (0, 0), (0, -.1)]
            fixationCross = visual.ShapeStim(experiment_window, vertices=fixationCross_coordinates,
                                             units='cm', size=4, closeShape=False, lineWidth=2, pos=(0, 0))

            trialClock.reset()
            trial_still_running = True

            while trial_still_running:
                fixationCross.draw()
                experiment_window.flip()
                core.wait(0.5)
                fixationCross.draw()
                experiment_window.flip()
                nFrame = 0

                stimuliClock = core.Clock()
                stimuliClock.reset()

                for i, j in zip(trial['lumSeqL'], trial['lumSeqR']):
                    barL_coordinates = [(-5.75, -2.05), (-5.75, 2.05), (-5.35, 2.05), (-5.35, -2.05)]
                    barL = visual.ShapeStim(experiment_window, vertices=barL_coordinates, units='cm',
                                            size=1, closeShape=True, lineWidth=2, pos=(0, 0), lineColor=None,
                                            fillColor=i, fillColorSpace='rgb255')
                    barR_coordinates = [(5.35, -2.05), (5.35, 2.05), (5.75, 2.05), (5.75, -2.05)]
                    barR = visual.ShapeStim(experiment_window, vertices=barR_coordinates, units='cm',
                                            size=1, closeShape=True, lineWidth=2, pos=(0, 0), lineColor=None,
                                            fillColor=j, fillColorSpace='rgb255')

                    fixationCross.draw()
                    barL.draw()
                    barR.draw()
                    t = experiment_window.flip()
                    nFrame = nFrame + 1
                    timeStim.append((nFrame, t, trial['SOA'], len(trial['lumSeqL'])))

                event.clearEvents()
                kb_resp = event.waitKeys(keyList=['c', 'm'])  # m = anderes ; c = gleich
                kb_resp_RT = stimuliClock.getTime()
                if kb_resp:
                    print(kb_resp)
                    kb_resp = kb_resp[0]  # key not a list of them
                    core.wait(0.001)  # make sure event was processed
                    trial_still_running = False
                    end_time = trialClock.getTime()
                    # record total response accuracy
                    if kb_resp == trial['corrResp']:
                        accuracyCounter = accuracyCounter + 1
                    elif kb_resp != trial['corrResp']:
                        accuracyCounter = accuracyCounter + 0

                checkForEscape()
                experiment_window.flip()

            trials.addData('Trial Number', counter)
            trials.addData('subjResp', kb_resp)
            trials.addData('respRT', kb_resp_RT)
            trials.addData('Trial Start', start_time)
            trials.addData('Trial End', end_time)
            trials.addData('Trial Duration', end_time - start_time)
            thisExp.nextEntry()

        if counter == 52:  # 52 trials per block
            print('Block is done.')
            block_end = blockClock.getTime()
            blockMessage = insertText('Ende Aufgabenblock. Drücken Sie die Leertaste, um fortzufahren.\n'
                                      'Drücken Sie „c“ für „gleichzeitig“ oder „m“ für „nicht gleichzeitig“.')
            blockMessage.draw()
            experiment_window.flip()
            core.wait(5)
            event.clearEvents()
            kb_resp_continue = event.waitKeys(keyList=['space'])
            if kb_resp_continue:
                kb_resp_continue = kb_resp_continue[0]  # key not a list of them
                core.wait(0.001)  # make sure event was processed
                block_still_running = False
            checkForEscape()

        blocks.addData('Block Number', blockCounter)
        blocks.addData('Block Start', block_start)
        blocks.addData('Block End', block_end)
        blocks.addData('Block Duration', block_end - block_start)
        thisExp.nextEntry()

# Write a csv of the frame info for each EXPERIMENTAL stimuli
# ---- includes frame number (frameN), time of the window flip based on a global clock (t),
# ---- the SOA condition (SOA), and the length of the luminance sequence (len(trial[lumSeq])

frameFile = thisDir + os.sep + u'data/frameseries/%s_%s_%s_%s_frameseries-exp.csv' % (
expName2, subject[0], subject[1], expInfo['date'])
f = open(frameFile, 'w')
for t in timeStim:
    line = ','.join(str(x) for x in t)
    f.write(line + '\n')
f.close()

# Preliminary Computations
# Calculate, print, and store the response accuracy for total trial and per trial condition
accuracyPercentage = (
                                 accuracyCounter / expTrialCounter) * 100  # should count the amount that is correct and divide by total trial number
print('accuracy percentage: ' + str(accuracyPercentage))
thisExp.addData('Accuracy %', accuracyPercentage)

# -------------------------------------------------------
# -------------------------------------------------------
# Initialize end of experiment stimuli

end_of_experiment = insertInstructionText('Der „Perceptual Simultaneity Task“ ist beendet.')

endExpClock = core.Clock()
endExpTimer = core.CountdownTimer()
start_time = 0

endExp_still_running = True

endExpClock.reset()

endExpComponents = [end_of_experiment]
initialize(endExpComponents)

# Run end of experiment sequence
while endExp_still_running:
    start_time = endExpClock.getTime()

    if start_time > 0 - frameTolerance and end_of_experiment.status == NOT_STARTED:
        start_time = endExpClock.getTime()
        end_of_experiment.tStart = start_time
        runEndExp(end_of_experiment)
        endExpTime = endExpClock.getTime()
        end_of_experiment.tStop = end_of_experiment.tStart + endExpTime

    experiment_window.flip()

    finalize(endExpComponents)
    end_time = endExpClock.getTime()
    endExp_still_running = False

endTrial(endExpComponents)

thisExp.addData('end_of_experiment.started', end_of_experiment.tStart)
thisExp.addData('end_of_experiment.stopped', end_of_experiment.tStop)
thisExp.nextEntry()

thisExp.addData('Exp Duration', expClock.getTime())

logging.flush()
experiment_window.close()
core.quit()
