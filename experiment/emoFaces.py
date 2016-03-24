#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
 ________    _______    ___       __           ________  ________   ________   _______    ________      
|\   ___  \ |\  ___ \  |\  \     |\  \        |\  _____\|\   __  \ |\   ____\ |\  ___ \  |\   ____\     
\ \  \\ \  \\ \   __/| \ \  \    \ \  \       \ \  \__/ \ \  \|\  \\ \  \___| \ \   __/| \ \  \___|_    
 \ \  \\ \  \\ \  \_|/__\ \  \  __\ \  \       \ \   __\ \ \   __  \\ \  \     \ \  \_|/__\ \_____  \   
  \ \  \\ \  \\ \  \_|\ \\ \  \|\__\_\  \       \ \  \_|  \ \  \ \  \\ \  \____ \ \  \_|\ \\|____|\  \  
   \ \__\\ \__\\ \_______\\ \____________\       \ \__\    \ \__\ \__\\ \_______\\ \_______\ ____\_\  \ 
    \|__| \|__| \|_______| \|____________|        \|__|     \|__|\|__| \|_______| \|_______||\_________\
                                                                                            \|_________|
"""


from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'facesParametric'  # from the Builder filename that created this script
expInfo = {u'participant': u'', u'group': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Check whether the chosen participant number is valid
myDlg = gui.Dlg(title="FEHLER")
myDlg.addText(u'Vp-Nnummer zwischen 1 und 100 eingeben')
assert len(str(expInfo['participant'])) > 0, myDlg.show()
try:
    assert int(expInfo['participant']) in range(1,101), myDlg.show()
except:
    myDlg.show()

# Check whether a group membership has been defined
myDlg = gui.Dlg(title="FEHLER")
myDlg.addText(u' Gruppenzugehoerigkeit angeben')
assert len(str(expInfo['group'])) > 0, myDlg.show()

# Here, we check if the number of the current participant
# is odd or even, and we swap the button order accordingly
# (this also affects the result computation, so the 'angry'
# button is different for the two versions)

if int(expInfo['participant'])%2 == 1:
    # odd participant numbers have buttons assigned fear-anger
    mainInstructText = u'Im nachfolgenden Experiment werden Sie nacheinander einzelne Gesichter sehen.\nSie m\xfcssen jeweils entscheiden, ob das gezeigt Gesicht einen\n\xc4NGSTLICHEN oder \xc4RGERLICHEN Ausdruck hat.\n\nEntscheiden Sie sich bei jedem gezeigten Gesicht f\xfcr einen der beiden m\xf6glichen Emotionsausdr\xfccke.'
    buttonInstructText = u'Dr\xfccken Sie die LINKE Maustaste,\nwenn das Gesicht eher \xc4NGSTLICH ist.\n\nDr\xfccken Sie die RECHTE Maustaste,\nwenn das Gesicht eher \xc4RGERLICH ist.'
    # angry judgement on right mouse button
    targetButton = 2
else:
    # even participant numbers have button assigments anger-fear
    mainInstructText = u'Im nachfolgenden Experiment werden Sie nacheinander einzelne Gesichter sehen.\nSie m\xfcssen jeweils entscheiden, ob das gezeigt Gesicht einen\n \xc4RGERLICHEN oder \xc4NGSTLICHEN Ausdruck hat.\n\nEntscheiden Sie sich bei jedem gezeigten Gesicht f\xfcr einen der beiden m\xf6glichen Emotionsausdr\xfccke.'
    buttonInstructText = u'Dr\xfccken Sie die LINKE Maustaste,\nwenn das Gesicht eher \xc4RGERLICH ist.\n\nDr\xfccken Sie die RECHTE Maustaste,\nwenn das Gesicht eher \xc4NGSTLICH ist.'
    # angry judgement on left mouse button
    targetButton = 0

# from the number defined in the prompt window, we derive
# which array files (pt1 & pt2) should be fetched for the
# current participant (this works for number from 1 to 999,
# but of course the array file must also exist!)

thisParticipant = 'arrays/p'+ ('00' + str(expInfo['participant']))[-3:]
pt1Conditions = thisParticipant +'pt1.csv'
pt2Conditions = thisParticipant +'pt2.csv'

countDict = {}
hitsDict = {}


# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s_%s' %(expInfo['group'],expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=[1280, 1024], fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='cm')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "mainInstruct"
mainInstructClock = core.Clock()
mainText = visual.TextStim(win=win, ori=0, name='mainText',
    text=mainInstructText,    font='Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "buttonInstruct"
buttonInstructClock = core.Clock()
buttonText = visual.TextStim(win=win, ori=0, name='buttonText',
    text=buttonInstructText,    font='Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "startScreen"
startScreenClock = core.Clock()
startText = visual.TextStim(win=win, ori=0, name='startText',
    text='Falls Sie noch Fragen haben,\nwenden Sie sich bitte an die Versuchsleiterin.\n\nWeiter mit ENTER.',    font='Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "mainTrial"
mainTrialClock = core.Clock()
faceImg = visual.ImageStim(win=win, name='faceImg',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[10.12,13.72],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouseResp = event.Mouse(win=win,visible=False)
x, y = [None, None]

# Initialize components for Routine "forcedPause"
forcedPauseClock = core.Clock()
pauseText = visual.TextStim(win=win, ori=0, name='pauseText',
    text=u'Zeit f\xfcr eine kurze Pause.',    font='Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "resumeExperiment"
resumeExperimentClock = core.Clock()
resumeText = visual.TextStim(win=win, ori=0, name='resumeText',
    text='Weiter mit ENTER.',    font='Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "mainTrial"
mainTrialClock = core.Clock()
faceImg = visual.ImageStim(win=win, name='faceImg',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[10.12,13.72],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouseResp = event.Mouse(win=win,visible=False)
x, y = [None, None]

# Initialize components for Routine "endInstruct"
endInstructClock = core.Clock()
endText = visual.TextStim(win=win, ori=0, name='endText',
    text='Dieser Teil des Experiments ist nun zu Ende.\nVielen Dank!\n\nWenden Sie sich bitte an die Versuchsleiterin.',    font='Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)



################################ BASIC EMOZ ##


# Initialize components for Routine "basicInstruct"
basicInstructClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u"Im nachfolgenden Experiment werden Sie nacheinander einzelne Gesichter sehen.\n\nSie m\xfcssen jeweils entscheiden, welchen Ausdruck das gezeigte Gesicht hat.\n\nZur Auswahl stehene Ihnen hierbei die folgenden M\xf6glichkeiten:\nFreude\nAngst\n\xc4rger\nTrauer\nEkel\n\xdcberraschung\nNeutral\n\nEntscheiden Sie sich bei jedem gezeigten Gesicht f\xfcr einen der \nm\xf6glichen Gesichtsausdr\xfccke.",    font='Arial',
    pos=[0, 0], height=0.8, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "basicTrial"
basicTrialClock = core.Clock()
basicImage = visual.ImageStim(win=win, name='basicImage',
    image='sin', mask=None,
    ori=0, pos=[0, 1], size=[10.12,13.72],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

basicRating1 = visual.RatingScale(win=win, name='basicRating1', marker=u'hover', size=0.6, pos=[0.0, -0.5], choices=[u'Freude', u'Trauer'], tickHeight=-1, disappear=True)
basicRating2 = visual.RatingScale(win=win, name='basicRating2', marker=u'hover', size=0.6, pos=[0.0, -0.6], choices=[u'Angst', u'\xc4rger'], tickHeight=-1, singleClick=True, disappear=True)
basicRating3 = visual.RatingScale(win=win, name='basicRating3', marker=u'hover', size=0.6, pos=[0.0, -0.7], choices=[u'Ekel', u'\xdcberraschung'], tickHeight=-1, singleClick=True, disappear=True)
basicRating4 = visual.RatingScale(win=win, name='basicRating4', marker=u'hover', size=0.6, pos=[0.0, -0.8], choices=[u' ',u'Neutral', u' '], tickHeight=-1, singleClick=True, disappear=True)

# Initialize components for Routine "basicWait"
basicWaitClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "basicEnd"
basicEndClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=u'Danke. Das war der erste Teil.\nDr\xfccken Sie ENTER um zum n\xe4chsten Teil zu kommen',    font=u'Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
    
    
    
    
###############################################################################


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 




#############################################



#------Prepare to start Routine "basicInstruct"-------
t = 0
basicInstructClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
basicInstructComponents = []
basicInstructComponents.append(text)
basicInstructComponents.append(key_resp_2)
for thisComponent in basicInstructComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "basicInstruct"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = basicInstructClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        key_resp_2.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in basicInstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "basicInstruct"-------
for thisComponent in basicInstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
   key_resp_2.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "basicInstruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
basicLoop = data.TrialHandler(nReps=1, method='fullRandom', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('./arrays/imgList.csv'),
    seed=None, name='basicLoop')
thisExp.addLoop(basicLoop)  # add the loop to the experiment
thisBasicLoop = basicLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBasicLoop.rgb)
if thisBasicLoop != None:
    for paramName in thisBasicLoop.keys():
        exec(paramName + '= thisBasicLoop.' + paramName)

for thisBasicLoop in basicLoop:
    currentLoop = basicLoop
    # abbreviate parameter names if possible (e.g. rgb = thisBasicLoop.rgb)
    if thisBasicLoop != None:
        for paramName in thisBasicLoop.keys():
            exec(paramName + '= thisBasicLoop.' + paramName)
    
    #------Prepare to start Routine "basicTrial"-------
    
    
    ###########
    # resetting the rating scales each time, so that the last response isnt visible
    
    basicRating1 = visual.RatingScale(win=win, name='basicRating1', marker=u'hover', size=0.6, pos=[0.0, -0.5], choices=[u'Freude', u'Trauer'], tickHeight=-1, disappear=True)
    basicRating2 = visual.RatingScale(win=win, name='basicRating2', marker=u'hover', size=0.6, pos=[0.0, -0.6], choices=[u'Angst', u'\xc4rger'], tickHeight=-1, singleClick=True, disappear=True)
    basicRating3 = visual.RatingScale(win=win, name='basicRating3', marker=u'hover', size=0.6, pos=[0.0, -0.7], choices=[u'Ekel', u'\xdcberraschung'], tickHeight=-1, singleClick=True, disappear=True)
    basicRating4 = visual.RatingScale(win=win, name='basicRating4', marker=u'hover', size=0.6, pos=[0.0, -0.8], choices=[u' ',u'Neutral', u' '], tickHeight=-1, singleClick=True, disappear=True)

    ###########
    
    t = 0
    basicTrialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    basicImage.setImage(img)
    basicRating1.reset()
    basicRating2.reset()
    basicRating3.reset()
    basicRating4.reset()
    # keep track of which components have finished
    basicTrialComponents = []
    basicTrialComponents.append(basicImage)
    basicTrialComponents.append(basicRating1)
    basicTrialComponents.append(basicRating2)
    basicTrialComponents.append(basicRating3)
    basicTrialComponents.append(basicRating4)
    for thisComponent in basicTrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    
    # ugly hack: the labels need to be renamed as the "umlaute" cannot be saved to csv 
    basicRating1.choices = ['HAP', 'SAD']
    basicRating2.choices = ['FEA', 'ANG']
    basicRating3.choices = ['DIS', 'SUP']
    basicRating4.choices = ['dummy','NTR', 'dummy']
    #-------Start Routine "basicTrial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = basicTrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *basicImage* updates
        if t >= 0 and basicImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            basicImage.tStart = t  # underestimates by a little under one frame
            basicImage.frameNStart = frameN  # exact frame index
            basicImage.setAutoDraw(True)
        if basicImage.status == STARTED and t >= (0 + (4.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            basicImage.setAutoDraw(False)
        # *basicRating1* updates
        if t >= 0.5 and basicRating1.status == NOT_STARTED:
            # keep track of start time/frame for later
            basicRating1.tStart = t  # underestimates by a little under one frame
            basicRating1.frameNStart = frameN  # exact frame index
            basicRating1.setAutoDraw(True)
        continueRoutine &= basicRating1.noResponse  # a response ends the trial
        # *basicRating2* updates
        if t >= 0.5 and basicRating2.status == NOT_STARTED:
            # keep track of start time/frame for later
            basicRating2.tStart = t  # underestimates by a little under one frame
            basicRating2.frameNStart = frameN  # exact frame index
            basicRating2.setAutoDraw(True)
        continueRoutine &= basicRating2.noResponse  # a response ends the trial
        # *basicRating3* updates
        if t >= 0.5 and basicRating3.status == NOT_STARTED:
            # keep track of start time/frame for later
            basicRating3.tStart = t  # underestimates by a little under one frame
            basicRating3.frameNStart = frameN  # exact frame index
            basicRating3.setAutoDraw(True)
        continueRoutine &= basicRating3.noResponse  # a response ends the trial
        # *basicRating4* updates
        if t >= 0.5 and basicRating4.status == NOT_STARTED:
            # keep track of start time/frame for later
            basicRating4.tStart = t  # underestimates by a little under one frame
            basicRating4.frameNStart = frameN  # exact frame index
            basicRating4.setAutoDraw(True)
        continueRoutine &= basicRating4.noResponse  # a response ends the trial
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in basicTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "basicTrial"-------
    for thisComponent in basicTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for basicLoop (TrialHandler)
    basicLoop.addData('basicRating1.response', basicRating1.getRating())
    basicLoop.addData('basicRating1.rt', basicRating1.getRT())
    # store data for basicLoop (TrialHandler)
    basicLoop.addData('basicRating2.response', basicRating2.getRating())
    basicLoop.addData('basicRating2.rt', basicRating2.getRT())
    # store data for basicLoop (TrialHandler)
    basicLoop.addData('basicRating3.response', basicRating3.getRating())
    basicLoop.addData('basicRating3.rt', basicRating3.getRT())
    # store data for basicLoop (TrialHandler)
    basicLoop.addData('basicRating4.response', basicRating4.getRating())
    basicLoop.addData('basicRating4.rt', basicRating4.getRT())
    # the Routine "basicTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "basicWait"-------
    t = 0
    basicWaitClock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    basicWaitComponents = []
    basicWaitComponents.append(ISI)
    for thisComponent in basicWaitComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "basicWait"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = basicWaitClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(5.0)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in basicWaitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "basicWait"-------
    for thisComponent in basicWaitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'basicLoop'


#------Prepare to start Routine "basicEnd"-------
t = 0
basicEndClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
basicEndComponents = []
basicEndComponents.append(text_2)
basicEndComponents.append(key_resp_3)
for thisComponent in basicEndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "basicEnd"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = basicEndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        key_resp_3.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in basicEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "basicEnd"-------
for thisComponent in basicEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
   key_resp_3.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "basicEnd" was not non-slip safe, so reset the non-slip timer
#routineTimer.reset()
#win.close()
#core.quit()


##############################################
mouseResp = event.Mouse(win=win,visible=False)


#------Prepare to start Routine "mainInstruct"-------
t = 0
mainInstructClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
mainInstructComponents = []
mainInstructComponents.append(mainText)
mainInstructComponents.append(key_resp_2)
for thisComponent in mainInstructComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "mainInstruct"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = mainInstructClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *mainText* updates
    if t >= 0.0 and mainText.status == NOT_STARTED:
        # keep track of start time/frame for later
        mainText.tStart = t  # underestimates by a little under one frame
        mainText.frameNStart = frameN  # exact frame index
        mainText.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        key_resp_2.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mainInstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "mainInstruct"-------
for thisComponent in mainInstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
   key_resp_2.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "mainInstruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "buttonInstruct"-------
t = 0
buttonInstructClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
buttonInstructComponents = []
buttonInstructComponents.append(buttonText)
buttonInstructComponents.append(key_resp_3)
for thisComponent in buttonInstructComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "buttonInstruct"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = buttonInstructClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *buttonText* updates
    if t >= 0.0 and buttonText.status == NOT_STARTED:
        # keep track of start time/frame for later
        buttonText.tStart = t  # underestimates by a little under one frame
        buttonText.frameNStart = frameN  # exact frame index
        buttonText.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        key_resp_3.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in buttonInstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "buttonInstruct"-------
for thisComponent in buttonInstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
   key_resp_3.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "buttonInstruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "startScreen"-------
t = 0
startScreenClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
startScreenComponents = []
startScreenComponents.append(startText)
startScreenComponents.append(key_resp_4)
for thisComponent in startScreenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "startScreen"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = startScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *startText* updates
    if t >= 0.0 and startText.status == NOT_STARTED:
        # keep track of start time/frame for later
        startText.tStart = t  # underestimates by a little under one frame
        startText.frameNStart = frameN  # exact frame index
        startText.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        key_resp_4.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "startScreen"-------
for thisComponent in startScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
   key_resp_4.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "startScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(pt1Conditions),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)

    #------Prepare to start Routine "mainTrial"-------
    t = 0
    mainTrialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    faceImg.setImage(img)
    # setup some python lists for storing info about the mouseResp
    mouseResp.x = []
    mouseResp.y = []
    mouseResp.leftButton = []
    mouseResp.midButton = []
    mouseResp.rightButton = []
    mouseResp.time = []
    # keep track of which components have finished
    mainTrialComponents = []
    mainTrialComponents.append(faceImg)
    mainTrialComponents.append(mouseResp)
    for thisComponent in mainTrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "mainTrial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = mainTrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *faceImg* updates
        if t >= 0.0 and faceImg.status == NOT_STARTED:
            # keep track of start time/frame for later
            faceImg.tStart = t  # underestimates by a little under one frame
            faceImg.frameNStart = frameN  # exact frame index
            faceImg.setAutoDraw(True)
        # *mouseResp* updates
        if t >= 0.3 and mouseResp.status == NOT_STARTED: ####################################
            # keep track of start time/frame for later
            mouseResp.tStart = t  # underestimates by a little under one frame
            mouseResp.frameNStart = frameN  # exact frame index
            mouseResp.status = STARTED
            event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
        if mouseResp.status == STARTED:  # only update if started and not stopped!
            buttons = mouseResp.getPressed()
            if sum(buttons) > 0:  # ie if any button is pressed
                x, y = mouseResp.getPos()
                mouseResp.x.append(x)
                mouseResp.y.append(y)
                mouseResp.leftButton.append(buttons[0])
                mouseResp.midButton.append(buttons[1])
                mouseResp.rightButton.append(buttons[2])
                mouseResp.time.append(mainTrialClock.getTime())
                
                
                
                
                # add a counter
                for morph in ['_00_','_01_','_02_','_03_','_04_','_05_','_06_','_07_','_08_','_09_','_10_']:
                    if morph in img:
                        try:
                            countDict[morph] += 1
                        except:
                            countDict[morph] = 1
                        if buttons[targetButton] == 1:
                            try:
                                hitsDict[morph]+=1
                            except:
                                hitsDict[morph]=1
                                
                # abort routine on response
                continueRoutine = False
                
                # ADDED THE ESC COMMAND INTO THE LOOP, SO WE CAN QUIT ANYTIME
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mainTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "mainTrial"-------
    for thisComponent in mainTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('mouseResp.x', mouseResp.x[0])
    trials.addData('mouseResp.y', mouseResp.y[0])
    trials.addData('mouseResp.leftButton', mouseResp.leftButton[0])
    trials.addData('mouseResp.midButton', mouseResp.midButton[0])
    trials.addData('mouseResp.rightButton', mouseResp.rightButton[0])
    trials.addData('mouseResp.time', mouseResp.time[0])
    # the Routine "mainTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


#------Prepare to start Routine "forcedPause"-------
t = 0
forcedPauseClock.reset()  # clock 
frameN = -1
routineTimer.add(30.000000)
# update component parameters for each repeat
# keep track of which components have finished
forcedPauseComponents = []
forcedPauseComponents.append(pauseText)
for thisComponent in forcedPauseComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "forcedPause"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = forcedPauseClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pauseText* updates
    if t >= 0.0 and pauseText.status == NOT_STARTED:
        # keep track of start time/frame for later
        pauseText.tStart = t  # underestimates by a little under one frame
        pauseText.frameNStart = frameN  # exact frame index
        pauseText.setAutoDraw(True)
    if pauseText.status == STARTED and t >= (0.0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
        pauseText.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in forcedPauseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "forcedPause"-------
for thisComponent in forcedPauseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "resumeExperiment"-------
t = 0
resumeExperimentClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_5.status = NOT_STARTED
# keep track of which components have finished
resumeExperimentComponents = []
resumeExperimentComponents.append(resumeText)
resumeExperimentComponents.append(key_resp_5)
for thisComponent in resumeExperimentComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "resumeExperiment"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = resumeExperimentClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *resumeText* updates
    if t >= 0.0 and resumeText.status == NOT_STARTED:
        # keep track of start time/frame for later
        resumeText.tStart = t  # underestimates by a little under one frame
        resumeText.frameNStart = frameN  # exact frame index
        resumeText.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # underestimates by a little under one frame
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        key_resp_5.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in resumeExperimentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "resumeExperiment"-------
for thisComponent in resumeExperimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
   key_resp_5.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "resumeExperiment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(pt2Conditions),
    seed=None, name='trials2')
thisExp.addLoop(trials2)  # add the loop to the experiment
thisTrials2 = trials2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrials2.rgb)
if thisTrials2 != None:
    for paramName in thisTrials2.keys():
        exec(paramName + '= thisTrials2.' + paramName)

for thisTrials2 in trials2:
    currentLoop = trials2
    # abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
    if thisTrials2 != None:
        for paramName in thisTrials2.keys():
            exec(paramName + '= thisTrials2.' + paramName)
    
    #------Prepare to start Routine "mainTrial"-------
    t = 0
    mainTrialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    faceImg.setImage(img)
    # setup some python lists for storing info about the mouseResp
    mouseResp.x = []
    mouseResp.y = []
    mouseResp.leftButton = []
    mouseResp.midButton = []
    mouseResp.rightButton = []
    mouseResp.time = []
    # keep track of which components have finished
    mainTrialComponents = []
    mainTrialComponents.append(faceImg)
    mainTrialComponents.append(mouseResp)
    for thisComponent in mainTrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "mainTrial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = mainTrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *faceImg* updates
        if t >= 0.0 and faceImg.status == NOT_STARTED:
            # keep track of start time/frame for later
            faceImg.tStart = t  # underestimates by a little under one frame
            faceImg.frameNStart = frameN  # exact frame index
            faceImg.setAutoDraw(True)
            
        # *mouseResp* updates
        if t >= 0.3 and mouseResp.status == NOT_STARTED: #############################################
            # keep track of start time/frame for later
            mouseResp.tStart = t  # underestimates by a little under one frame
            mouseResp.frameNStart = frameN  # exact frame index
            mouseResp.status = STARTED
            event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
        if mouseResp.status == STARTED:  # only update if started and not stopped!
            buttons = mouseResp.getPressed()
            if sum(buttons) > 0:  # ie if any button is pressed
                x, y = mouseResp.getPos()
                mouseResp.x.append(x)
                mouseResp.y.append(y)
                mouseResp.leftButton.append(buttons[0])
                mouseResp.midButton.append(buttons[1])
                mouseResp.rightButton.append(buttons[2])
                mouseResp.time.append(mainTrialClock.getTime())
                
                # add a counter
                for morph in ['_00_','_01_','_02_','_03_','_04_','_05_','_06_','_07_','_08_','_09_','_10_']:
                    if morph in img:
                        try:
                            countDict[morph] += 1
                        except:
                            countDict[morph] = 1
                        if buttons[targetButton] == 1:
                            try:
                                hitsDict[morph]+=1
                            except:
                                hitsDict[morph]=1
                    
                # abort routine on response
                continueRoutine = False
        
                # ADDED THE ESC COMMAND INTO THE LOOP, SO WE CAN QUIT ANYTIME
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                    
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mainTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "mainTrial"-------
    for thisComponent in mainTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials2 (TrialHandler)
    trials2.addData('mouseResp.x', mouseResp.x[0])
    trials2.addData('mouseResp.y', mouseResp.y[0])
    trials2.addData('mouseResp.leftButton', mouseResp.leftButton[0])
    trials2.addData('mouseResp.midButton', mouseResp.midButton[0])
    trials2.addData('mouseResp.rightButton', mouseResp.rightButton[0])
    trials2.addData('mouseResp.time', mouseResp.time[0])
    
    # the Routine "mainTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials2'


#------Prepare to start Routine "endInstruct"-------
t = 0
endInstructClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_6.status = NOT_STARTED
# keep track of which components have finished
endInstructComponents = []
endInstructComponents.append(endText)
endInstructComponents.append(key_resp_6)
for thisComponent in endInstructComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "endInstruct"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = endInstructClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endText* updates
    if t >= 0.0 and endText.status == NOT_STARTED:
        # keep track of start time/frame for later
        endText.tStart = t  # underestimates by a little under one frame
        endText.frameNStart = frameN  # exact frame index
        endText.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 0.0 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t  # underestimates by a little under one frame
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        key_resp_6.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_6.keys = theseKeys[-1]  # just the last key pressed
            key_resp_6.rt = key_resp_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endInstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "endInstruct"-------
for thisComponent in endInstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# Initialize components for Routine "analysisCheck"
analysisCheckClock = core.Clock()
analysisText = visual.TextStim(win=win, ori=0, name='analysisText',
    text=str('00'+'\t'+str(countDict['_00_'])+'\t'+str(hitsDict['_00_'])+'\n'+
    '01'+'\t'+str(countDict['_01_'])+'\t'+str(hitsDict['_01_'])+'\n'+
    '02'+'\t'+str(countDict['_02_'])+'\t'+str(hitsDict['_02_'])+'\n'+
    '03'+'\t'+str(countDict['_03_'])+'\t'+str(hitsDict['_03_'])+'\n'+
    '04'+'\t'+str(countDict['_04_'])+'\t'+str(hitsDict['_04_'])+'\n'+
    '05'+'\t'+str(countDict['_05_'])+'\t'+str(hitsDict['_05_'])+'\n'+
    '06'+'\t'+str(countDict['_06_'])+'\t'+str(hitsDict['_06_'])+'\n'+
    '07'+'\t'+str(countDict['_07_'])+'\t'+str(hitsDict['_07_'])+'\n'+
    '08'+'\t'+str(countDict['_08_'])+'\t'+str(hitsDict['_08_'])+'\n'+
    '09'+'\t'+str(countDict['_09_'])+'\t'+str(hitsDict['_09_'])+'\n'+
    '10'+'\t'+str(countDict['_10_'])+'\t'+str(hitsDict['_10_'])), font='Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

#------Prepare to start Routine "analysisCheck"-------
t = 0
analysisCheckClock.reset()  # clock
frameN = -1
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_7.status = NOT_STARTED
# keep track of which components have finished
analysisCheckComponents = []
analysisCheckComponents.append(analysisText)
analysisCheckComponents.append(key_resp_7)
for thisComponent in analysisCheckComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "analysisCheck"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = analysisCheckClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *analysisText* updates
    if t >= 0.0 and analysisText.status == NOT_STARTED:
        # keep track of start time/frame for later
        analysisText.tStart = t  # underestimates by a little under one frame
        analysisText.frameNStart = frameN  # exact frame index
        analysisText.setAutoDraw(True)

    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t  # underestimates by a little under one frame
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        key_resp_7.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'return'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_7.keys = theseKeys[-1]  # just the last key pressed
            key_resp_7.rt = key_resp_7.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in analysisCheckComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "analysisCheck"-------
for thisComponent in analysisCheckComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
   key_resp_7.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# the Routine "analysisCheck" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
win.close()
core.quit()