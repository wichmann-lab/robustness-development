from psychopy import visual, core, clock, event, gui, data
from psychopy.tools.filetools import fromFile, toFile

import random as ran
import numpy as np
import math
import pandas as pd
import os
import sys
import csv
import time

# function to move up from a given path
def dir_up(path,n): # here 'path' is your path, 'n' is number of dirs up you want to go
    for _ in range(n):
        path = dir_up(path.rpartition("/")[0], 0) 
    return(path)

# CONSTANTS
#--------------------------------------------------------------------------#

# Please note that due to copy right issues, images are not publicity available on gitHub.
# But do not hesitate to contact me (omitted_for@anonymous.review) and I will be happy to share all 
# employed images in order to make the below code work as it is.

# paths:
CWD                     =       os.getcwd()
CWD_1UP                 =       dir_up(CWD,1)
CWD_3UP                 =       dir_up(CWD,3)
PATH_IMG                =       CWD_1UP+"/img/"
PATH_ICONS              =       CWD_1UP+"/img/icons/"
PATH_PROROTYPES         =       CWD_1UP+"/img/prototypes/"
PATH_CATEGORYCHECK      =       CWD_1UP+"/img/category_check/"
PATH_SNP_EX             =       CWD_1UP+"/img/condition_example/test_image_salt_and_pepper_noise.png"
PATH_EID_EX             =       CWD_1UP+"/img/condition_example/testimage_eidolon.png"
PATH_CC_EX              =       CWD_1UP+"/img/condition_example/car6-elephant3.png"
PATH_MASK               =       CWD_1UP+"/img/mask.png"
PATH_PRACTICE           =       CWD_1UP+"/img/practice/"
PATH_GAMIFICATION       =       CWD_1UP+"/img/gamification/"
PATH_STAR               =       CWD_1UP+"/img/gamification/star.png"
PATH_EMPTY_STAR         =       CWD_1UP+"/img/gamification/empty_star.png"
PATH_COIN               =       CWD_1UP+"/img/gamification/coin.png"
PATH_FLAGS              =       CWD_1UP+"/img/gamification/flags.png"
PATH_SPY_EMBLEM         =       CWD_1UP+"/img/gamification/spy.png"
PATH_SCIENTIST_EMBLEM   =       CWD_1UP+"/img/gamification/scientist.png"
PATH_SAFARI_EMBLEM       =      CWD_1UP+"/img/gamification/safari.png"
PATH_DETECTIVE_EMBLEM   =       CWD_1UP+"/img/gamification/detective.png"
PATH_DETECTIVE_MALE     =       CWD_1UP+"/img/gamification/detective_male.png"
PATH_DETECTIVE_FEMALE   =       CWD_1UP+"/img/gamification/detective_female.png"
PATH_SCIENTIST_MALE     =       CWD_1UP+"/img/gamification/scientist_male.png"
PATH_SCIENTIST_FEMALE   =       CWD_1UP+"/img/gamification/scientist_female.png"
PATH_SPY_MALE           =       CWD_1UP+"/img/gamification/spy_male.png"
PATH_SPY_FEMALE         =       CWD_1UP+"/img/gamification/spy_female.png"
PATH_SAFARI_MALE        =       CWD_1UP+"/img/gamification/safari_male.png"
PATH_SAFARI_FEMALE      =       CWD_1UP+"/img/gamification/safari_female.png"

PATH_METABLOCKS_SNP     =       CWD_1UP+"/img/test_images/snp_and_eid/metablocks/snp_metablocks/"
PATH_METABLOCKS_EID     =       CWD_1UP+"/img/test_images/snp_and_eid/metablocks/eid_metablocks/"
PATH_METABLOCKS_CC      =       CWD_1UP+"/img/test_images/cue_conflict/cue_conflict_metablocks/"

# durations 

FIXCROSS_DUR_SEQ        =       9
FIXCROSS_DUR_WHOLE      =       36
CIRCLE_DUR_SEQ          =       4
IMAGE_DUR               =       18
MASK_DUR                =       18 


# LISTS WITH FILENAMES
#--------------------------------------------------------------------------#

#icons images
icon_path_list = os.listdir(PATH_ICONS)
icon_path_list = [PATH_ICONS + x for x in icon_path_list]
icon_path_list.sort()

#prototype images
proto_path_list = os.listdir(PATH_PROROTYPES)
proto_path_list = [PATH_PROROTYPES + x for x in proto_path_list]
proto_path_list.sort()

# practice trials
practice_path_list = os.listdir(PATH_PRACTICE)
practice_path_list = [PATH_PRACTICE + x for x in practice_path_list]
practice_path_list.sort()

# category_check
category_check_path_list = os.listdir(PATH_CATEGORYCHECK)
category_check_path_list = [PATH_CATEGORYCHECK + x for x in category_check_path_list]
category_check_path_list.sort()


# EXPERIMENT INFORMATIONS
#--------------------------------------------------------------------------#

#creates dict for expInfo
expInfo = { "subj": '',
            "session": "",
           'codename': '',
           'age': '',
           'grade': '',
           'schoolname': '',
           'gender': '',
           'languague': '',
           'handedness': '',
           'condition': '',
           }

#creates gui for entering expInfo
dlg1 = gui.DlgFromDict(dictionary=expInfo, title='Please Enter Paticipant Information')
if dlg1.OK == False:
    print('user cancelled')
    core.quit()


# checks wheter gender information was provided correctly
while expInfo['gender'] != 'f' and expInfo['gender'] != 'm':
    dlg2 = gui.Dlg(title='invalid gender information')
    dlg2.addText('You provided \"%s\" as gender information.\nPlease use \"f\" or \"m\".' % expInfo['gender'])
    dlg2.addField('gender:' '')
    gender = dlg2.show()
    expInfo['gender'] = gender[0] 
    if dlg2.OK == False:
        print('user cancelled')
        core.quit()

# checks wheter condition information was provided correctly
while expInfo['condition'] != 'snp' and expInfo['condition'] != 'eid' and expInfo['condition'] != 'cc':
    dlg3 = gui.Dlg(title='invalid condition information')
    dlg3.addText('You provided \"%s\" as condition information.\nPlease specify condition with \"eid\" for eidolon, \n\"snp\" for salt and pepper or \"cc\" for cue-conflict.' % expInfo['condition'])
    dlg3.addField('condition:' '')
    condition = dlg3.show()
    expInfo['condition'] = condition[0] 
    if dlg3.OK == False:
        print('user cancelled')
        core.quit()

# checks wheter age information was provided

while True:

    try: 
        int(expInfo['age'])
        break
    except:
        dlg3 = gui.Dlg(title='invalid age information')
        dlg3.addText('You provided a non valid age information.\nPlease specify age with a number between 1 and 80')
        dlg3.addField('age:' '')
        age = dlg3.show()
        expInfo['age'] = age[0]
        if dlg3.OK == False:
            print('user cancelled')
            core.quit()
        

# adds date and a experiment name to exptInfo
expInfo['date'] = data.getDateStr()
expInfo['expName'] = 'noisyChildren'

# Ensures that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

#creates a file Name for rawData and supplementData
fileName = expInfo['subj'] + "_" + expInfo['date']

# creates a file name to be used by the experiment handler 
emrgencyFileName = CWD_3UP +"/data/noisy_children/"+ os.sep + \
    u'emergency_data/%s_%s-%s_%s_%s' % (expInfo["expName"], "subject", expInfo['subj'], "session", expInfo["session"]) 
                                                                # this file name is then used by the experiment handler. it saves all data even
                                                                 # in case of a crash (the other two data files - rawData and supplementData - 
                                                                 # won't get written in case of a crash) because it contains all the data it's stored locally
                                                                 # and not in the gitHub repo

# Checks whetere file already exists
if os.path.exists(fileName):
    sys.exit("Filename " + fileName + " already exists!")

# sets experiment name

if expInfo['condition'] == 'cc':
    expName = 'kids-cueconflict-experiment'
elif expInfo['condition'] == 'snp':
    expName = 'kids-noise-experiment'
elif expInfo['condition'] == 'eid':
    expName = 'kids-eidolon-experiment'

# get age groups

if int(expInfo['age'])<=6:
    ageGroup = str(1)
    starBonus = 3
elif int(expInfo['age'])<=9:
    ageGroup = str(2)
    starBonus = 2
elif int(expInfo['age'])<=12:
    ageGroup = str(3)
    starBonus = 1
elif int(expInfo['age'])>12:
    ageGroup = str(4)
    starBonus = 0

# creates the rawData cvs file to store the subjects main data 
rawData = open(CWD_1UP+ "/data/raw_data/" + expName + "_" + "subject-" +expInfo['subj'] +  "_" + "session_" + expInfo['session'] +'.csv', 'w')
rawData.write("subj,session,trial,rt,object_response,category,condition,imagename, age, block, coverstory,accuracy_within,acurracy_overall\n")


# creates the supplement cvs file to store the subjects supplement data. it's stored locally because it contains sentive data
supplementData = open (CWD_3UP+ "/data/noisy_children/supplement_data/" + expName + "_" + "subject-" +expInfo['subj'] +  "_" + "session_" + expInfo['session'] + ".cvs", "w")
supplementData.write("subj,codename,age,grade,gender,handedness,languague,school\n")
supplementData.write("%s,%s,%s,%s,%s,%s,%s,%s\n" %(expInfo['subj'], expInfo['codename'], expInfo['age'],expInfo['grade'],
expInfo['gender'],expInfo['handedness'],expInfo['languague'],expInfo['schoolname']))


# EXPERIMENT HANDLER
#--------------------------------------------------------------------------#
thisExp = data.ExperimentHandler(name=expInfo['expName'],
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath=CWD,
                                 savePickle=False, saveWideText=True, dataFileName = emrgencyFileName)

# WINDOW SETUP
#--------------------------------------------------------------------------#
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[121.86,121.86,121.86], colorSpace='rgb255',
    blendMode='avg', useFBO=True,
    units='pix')

# STIMULI AND OTER OBJECTS EMPLOYED IN MULTIPLE STEPS OF EXPERIENT
#--------------------------------------------------------------------------#

# plz note: specific stimuli used for only a certain steps of the experiment (category check, practice trials, test trials)
# are defined at the begining of each step

# fixation Cross

fixCross = cross = visual.ShapeStim (win = win, units ='pix', lineColor='white', fillColor="white", 
vertices=("cross"), pos=(0, 0), size=100)

# fixation circle

def make_square (vertices):
    return (visual.ShapeStim(
                        win=win, units='', lineWidth=1.5, lineColor=[142.2, 142.2, 142.2], lineColorSpace='rgb255', 
                        fillColor=[142.2, 142.2, 142.2], fillColorSpace='rgb255', 
                        vertices=vertices, opacity=1))


circleFull = visual.Circle(
    win=win,
    radius=60,
    edges = 128,
    fillColor = "white"
)

circleEmpty = visual.Circle(
    win=win,
    radius=60,
    edges = 128,
)

circleCount1 = make_square(((-300, -300), (0, 0), (-300, 0)))
circleCount2 = make_square(((-300, -300), (0, -300), (0, 0)))
circleCount3 = make_square(((0, -300), (300, -300), (0, 0)))
circleCount4 = make_square(((300, -300), (300, 0), (0, 0)))
circleCount5 = make_square(((0, 0), (300, 0), (300, 300)))
circleCount6 = make_square(((0, 0), (300, 300), (0, 300)))
circleCount7 = make_square(((-300, 300), (0, 0), (0, 300)))
circleCount8 = make_square(((-300, 0), (0, 0), (-300, 300)))

circleCounts = [circleCount8,circleCount1,circleCount2,circleCount3,circleCount4,circleCount5,circleCount6,circleCount7]

# mask

noise = visual.ImageStim(win, pos = (0, 0), size = 224, image=PATH_MASK)

# progress bar outline (sctual progress bar is defined when response screen is drawn. this is because it has to be adaptive with regard to the progress)

prog_bar_outline = visual.Rect(win, pos=(0,-350), size=(800,40), lineColor='White')

# white frame for score display

frameScore = visual.ShapeStim (win, units='', lineWidth=1.5, 
lineColor='white', lineColorSpace='rgb', fillColor=None, vertices=((-400, -300), (400, -300), (400, 300), (-400,300)))

# coin and star icons for score diplay

coin1 = visual.ImageStim(win, pos = (-260, 50), size=120, image=PATH_COIN)
star1 = visual.ImageStim(win, pos = (-260, 50), size=120, image=PATH_STAR)
coin2 = visual.ImageStim(win, pos = (-120, -240), size=50, image=PATH_COIN)
star2 = visual.ImageStim(win, pos = (45, -240), size=50, image=PATH_STAR)

def make_star(position):
    return(visual.ImageStim(win, pos = position, size=50, image=PATH_STAR))

## 10 stars for star score display of current block
star3 = make_star((-225,200))
star4 = make_star((-175,200))
star5 = make_star((-125,200))
star6 = make_star((-75,200))
star7 = make_star((-25,200))
star8 = make_star((25,200))
star9 = make_star((75,200))
star10 = make_star((125,200))
star11 = make_star((175,200))
star12 = make_star((225,200))

stars =[star3,star4,star5,star6,star7,star8,star9,star10,star11,star12] # list of stars

##10 empty stars for star score display of current block
def make_empty_star(position):
    return(visual.ImageStim(win, pos = position, size=50, opacity = 0.3, image=PATH_EMPTY_STAR))

star13 = make_empty_star((-225,200))
star14 = make_empty_star((-175,200))
star15 = make_empty_star((-125,200))
star16 = make_empty_star((-75,200))
star17 = make_empty_star((-25,200))
star18 = make_empty_star((25,200))
star19 = make_empty_star((75,200))
star20 = make_empty_star((125,200))
star21 = make_empty_star((175,200))
star22 = make_empty_star((225,200))

empty_stars = [star13,star14,star15,star16,star17,star18,star19,star20,star21,star22]


# coverstory

## emblem

safariEmblem1 = visual.ImageStim(win, pos = (-260, -100), size=120, image=PATH_SAFARI_EMBLEM)
safariEmblem2 = visual.ImageStim(win, pos = (215, -240), size=50, image=PATH_SAFARI_EMBLEM)
scientistEmblem1 = visual.ImageStim(win, pos = (-260, -100), size=120, image=PATH_SCIENTIST_EMBLEM)
scientistEmblem2 = visual.ImageStim(win, pos = (215, -240), size=50, image=PATH_SCIENTIST_EMBLEM)
spyEmblem1 = visual.ImageStim(win, pos = (-260, -100), size=120, image=PATH_SPY_EMBLEM)
spyEmblem2 = visual.ImageStim(win, pos = (215, -240), size=50, image=PATH_SPY_EMBLEM)
detectiveEmblem1 = visual.ImageStim(win, pos = (-260, -100), size=120, image=PATH_DETECTIVE_EMBLEM)
detectiveEmblem2 = visual.ImageStim(win, pos = (215, -240), size=50, image=PATH_DETECTIVE_EMBLEM)

## character

safariMale = visual.ImageStim(win, pos = (-600, 0), size=300, image=PATH_SAFARI_MALE)
safariFemale = visual.ImageStim(win, pos = (-600, 0), size=300, image=PATH_SAFARI_FEMALE)
scientistMale = visual.ImageStim(win, pos = (-200, 0), size=300, image=PATH_SCIENTIST_MALE)
scientistFemale = visual.ImageStim(win, pos = (-200, 0), size=300, image=PATH_SCIENTIST_FEMALE)
spyMale = visual.ImageStim(win, pos = (200, 0), size=300, image=PATH_SPY_MALE)
spyFemale = visual.ImageStim(win, pos = (200, 0), size=300, image=PATH_SPY_FEMALE)
detectiveMale = visual.ImageStim(win, pos = (600, 0), size=300, image=PATH_DETECTIVE_MALE)
deteciveFemale = visual.ImageStim(win, pos = (600, 0), size=300, image=PATH_DETECTIVE_FEMALE)

# response fields

# define a function to draw response fields. first argument should tak te form of ((a, b), (c, d), (e, f),(g,h)) and the second should be a value
# between 0 (completely transparent) and 1(not a single bit transparent)

def make_respond_field(vertices, opacity):
    return (visual.ShapeStim (win,units='', lineWidth=1.5, lineColor='white', lineColorSpace='rgb', fillColor="white", fillColorSpace='rgb', 
    vertices=vertices, opacity=opacity))

## define respond fields to choose coverstory

safariField = make_respond_field(((-650, -300), (-550, -300), (-550, -200),(-650,-200)),1)
scientistField = make_respond_field(((-250, -300), (-150, -300), (-150, -200),(-250,-200)),1)
spyField = make_respond_field(((250, -300), (150, -300), (150, -200),(250,-200)),1)
detectiveField = make_respond_field(((650, -300), (550, -300), (550, -200),(650,-200)),1)

characterFields = [safariField, scientistField, spyField, detectiveField] # list with all rsponsefields for coverstory

characterLables = ["safari", "scientist", "spy", "detective"]

## response screen layout for trials' reponse surface


## transparent response icons

def make_icon (position, image):
    return(visual.ImageStim(win, pos = position, size=125, image=PATH_ICONS + image))

knife = make_icon((-192,192), "knife.png")
bicycle = make_icon((-64,192), "bicycle.png")
bear = make_icon((64,192), "bear.png")
truck = make_icon((192,192), "truck.png")
airplane = make_icon((-192,64), "airplane.png")
clock = make_icon((-64,64), "clock.png")
boat = make_icon((64,64), "boat.png")
car = make_icon((192,64), "car.png")
keyboard = make_icon((-192,-64), "keyboard.png")
oven = make_icon((-64,-64), "oven.png")
cat = make_icon((64,-64), "cat.png")
bird = make_icon((192,-64), "bird.png")
elephant = make_icon((-192,-192), "elephant.png")
chair = make_icon((-64,-192), "chair.png")
bottle = make_icon((64,-192), "bottle.png")
dog = make_icon((192,-192), "dog.png")

## list of all icon stimuli

iconStimuli = [knife,bicycle,bear,truck,airplane,clock,boat,car,keyboard,oven,cat,bird,elephant,chair,bottle,dog]

## list of all category lables

categoryLables = ["knife","bicycle","bear","truck","airplane","clock","boat","car","keyboard","oven","cat","bird","elephant","chair","bottle","dog"]

## response fields for response surface

square0 = make_respond_field(((-256, 128), (-128, 128), (-128, 256),(-256,256)),0)
square1 = make_respond_field(((-128, 128), (0, 128), (0, 256),(-128,256)),0)
square2 = make_respond_field(((0, 128), (128, 128), (128, 256),(0,256)),0)
square3 = make_respond_field(((128, 128), (256, 128), (256, 256),(128,256)),0)
square4 = make_respond_field(((-256, 0), (-128, 0), (-128, 128),(-256,128)),0)
square5 = make_respond_field(((-128, 0), (0, 0), (0, 128),(-128,128)),0)
square6 = make_respond_field(((0, 0), (128, 0), (128, 128),(0,128)),0)
square7 = make_respond_field(((128, 0), (256, 0), (256, 128),(128,128)),0)
square8 = make_respond_field(((-256, -128), (-128, -128), (-128, 0),(-256,0)),0)
square9 = make_respond_field(((-128, -128), (0, -128), (0, 0),(-128,0)),0)
square10 = make_respond_field(((0, -128), (128, -128), (128, 0),(0,0)),0)
square11 = make_respond_field(((128, -128), (256, -128), (256, 0),(128,0)),0)
square12 = make_respond_field(((-256, -256), (-128, -256), (-128, -128),(-256,-128)),0)
square13 = make_respond_field(((-128, -256), (0, -256), (0, -128),(-128,-128)),0)
square14 = make_respond_field(((0, -256), (128, -256), (128, -128),(0,-128)),0)
square15 = make_respond_field(((128, -256), (256, -256), (256, -128),(128,-128)),0)

responseFields = [square0, square1, square2, square3, square4,square5, square6, square7, square8, square9,
square10, square11, square12, square13, square14, square15] # list of all response fields for response surface


## non response fields fields for response surface to prevent a crash when no actual response field is pressed.

square16 = make_respond_field(((-1200, -800), (-256, -800), (-256, 800),(-1200,800)),0)
square17 = make_respond_field(((-256, -800), (1200, -800), (1200, -252),(-256,-252)),0)
square18 = make_respond_field(((256, -252), (1200, -252), (1200, 800),(256,800)),0)
square19 = make_respond_field(((-256, 252), (256, 252), (256, 800),(-256,800)),0)

nonResponseFields = [square16, square17, square18, square19] # list with all nonresponse field for response surface

# "are you read" page

flags = visual.ImageStim(win, pos = (0, -50), image=PATH_FLAGS)
flagsSmall = visual.ImageStim(win, pos = (450, -350), size = 70, image=PATH_FLAGS)
ready = visual.TextStim (win, text="Bereit?!", height = 75, pos = (0, 250,))

# try again:

tryAgain = visual.TextStim (win, text="Uuuups", height = 90, pos = (0, 0,))


# COVERSTORY CHOICE
#--------------------------------------------------------------------------#

# adjusting characters for gender of participant

if expInfo["gender"] == "m":
    gender = "_male"
    safariCharacter = safariMale
    scientistCharacter = scientistMale
    spyCharacter = spyMale
    detectiveCharacter = detectiveMale

elif expInfo["gender"] == "f":
    gender = "_female"
    safariCharacter = safariFemale
    scientistCharacter = scientistFemale
    spyCharacter = spyFemale
    detectiveCharacter = deteciveFemale
else:
    print("please enter correct gender information: either f for female or m for male")
    core.quit()

# display characters an response fields

while True:

    mouseCharacter = event.Mouse(visible=True, win = win)

    safariCharacter.draw()
    scientistCharacter.draw()
    spyCharacter.draw()
    detectiveCharacter.draw()

    #draw repsonse field
    for field in characterFields:
        field.draw()
    win.flip()

    # making esc possible
    theseKeys = event.getKeys(keyList=['escape'])
    if len(theseKeys) > 0:
        win.close()
        core.quit()

    # record which response field is clicked
    for n, shape in enumerate(characterFields):
        if mouseCharacter.isPressedIn(shape):
            coverstory = characterLables[n]

    
    # move to category check
    buttons = mouseCharacter.getPressed()
    if buttons[0] != 0:
        mouseCharacter.setVisible(visible=False) # make mouse invisible again - minimize distraction while target stimulus is presented
        break


# set emblem according to coverstory
if coverstory == "safari":
    emblem1 = safariEmblem1
    emblem2 = safariEmblem2
elif coverstory == "scientist":
    emblem1 = scientistEmblem1
    emblem2 = scientistEmblem2
elif coverstory == "spy":
    emblem1 = spyEmblem1
    emblem2 = spyEmblem2
elif coverstory == "detective":
    emblem1 = detectiveEmblem1
    emblem2 = detectiveEmblem2

PATH_CHARACTER = PATH_GAMIFICATION + coverstory + gender +".png" # set path for character display on progress bar


# CATEGORY CHECK
# --------------------------------------------------------------------------#

for image in category_check_path_list:
    checkStim= visual.ImageStim(win, image= image)
    mouseCheck = event.Mouse(visible=False,win=win)

    while True:

        checkStim.draw()
        win.flip()
        
        # making esc possible
        theseKeys = event.getKeys(keyList=['escape'])
        if len(theseKeys) > 0:
            win.close()
            core.quit()

        # Check for response
        buttons = mouseCheck.getPressed()
        if buttons[0] != 0:
            break



# PRACTICE TRIALS
#--------------------------------------------------------------------------#

correctBlock = 0 #initialize value to count correct choices per practice block
count_practice_blocks = 0 # initialize value to count repetition of practice block

# allow agegroup 1 to pass practice trials eventhough they make more than 2 errors
if int(ageGroup) == 1:
    limit = 1
else:
    limit = 8

while correctBlock < limit: # repeat practice block if less than 8 choices were correct.

    count_practice_blocks = count_practice_blocks + 1 # add one for each time the while loop runs
 
    # create a list with paths for the images to be used in this block (drawing from all not used stimuli)
    images = []
    for imageName in os.listdir(CWD_1UP+'/img/test_images/snp_and_eid/unused_images'):
        images.append(CWD_1UP+'/img/test_images/snp_and_eid/unused_images/'+imageName)

    ran.seed(37)# plant random seed
    ran.shuffle(images)# shuffle image list randomly
    ran.seed(count_practice_blocks)# plant a new seed each time the practice block has to be repeated
    images = ran.sample(images,10) # sample 10 images from all unused images
    correct_answers = []

    # create a list with correct answers for the current block
    for image in images:
        correct_answer = (image.split("/")[-1]).split("_")[0]
        correct_answers.append(correct_answer)

    # stimuli
    practiceClock=core.Clock() # creates a clock to meassure rt
    practiceStim = visual.ImageStim(win, size = 224, image=images[0])# create a image stimulus

    # Preparation for loop

    trialsTotal = 0 # track number of total trials 
    correctTotal = 0 # track number of total correct trials

    trialsBlock = 0 # track number of trials in this block
    correctBlock = 0 # track number of correct trials in this block

    #set up trial handler for current block
    practiceTrials = data.TrialHandler(nReps=1, method='sequential',
        extraInfo=expInfo,
        trialList=images,
        seed=None, name='practiceTrials')

    # "are you ready?"

    while True:

        mouseReady = event.Mouse(visible=False,win=win)

        flags.draw()
        ready.draw()
        win.flip()

        # check for response
        buttons = mouseReady.getPressed()
        if buttons[0] != 0:
            break


    # Start of practice Loop //interates through condition list

    for thisTrial in practiceTrials:

        # progress bar settings and progress bar stimuli 
        progress = (trialsBlock+1) * 80 # sets parameter for progress bar in response field
        prog_bar = visual.Rect(win, pos=((-400 + (progress/2)),-350), size=(progress,40), lineColor='White',fillColor="white", fillColorSpace='rgb')
        character = visual.ImageStim(win, pos = ((-400+progress), -350), size=80, image=PATH_CHARACTER)


        # fixation circle
        for n in range(9):
            for frameN in range(CIRCLE_DUR_SEQ):
                circleFull.draw()
                for i in range(n):
                    circleCounts[i-1].draw()
                circleEmpty.draw()
                win.flip()

        # target stimulus presentation 18 frames --> 300ms

        practiceStim.setImage(images[trialsBlock])# set image for current trial by iterating through the images list

        for frameN in range(IMAGE_DUR):
            practiceStim.draw()
            win.flip()

        # white noise mask 18 frames -> 300ms    
        for frameN in range(MASK_DUR):
            noise.draw()
            win.flip()

        # get reaction time while children respond physically
        practiceClock.reset()
        while True:
            
            mouseReaction = event.Mouse(visible=False,win=win) # create mouse to grab rt when clicked

            win.flip()

            theseKeys = event.getKeys(keyList=['escape'])
            if len(theseKeys) > 0:
                win.close()
                core.quit()

            # check for response
            buttons = mouseReaction.getPressed()
            if buttons[0] != 0:
                rt = practiceClock.getTime()
                thisExp.addData('response.rt',rt)
                break

        # response screen

        mouseResponse = event.Mouse(visible=True,win=win, newPos = [-300,0]) # create mouse to choose a certain category
        handBrake = True # apply the handbreak to prevent loop from collapsing when the mouse ist clicked too fast in succesion

        # draw response surface
        while True: 

            #draw non response fields
            for field in nonResponseFields:
                field.draw()

            #draw repsonse field
            for field in responseFields:
                field.draw()

            #draw response layout (icons)
            for icon in iconStimuli:
                icon.draw()

            # draw progress bar
            prog_bar_outline.draw()
            prog_bar.draw()
            flagsSmall.draw()
            character.draw()
            win.flip()

            # enabling esc
            theseKeys = event.getKeys(keyList=['escape'])
            if len(theseKeys) > 0:
                win.close()
                core.quit()

            # continue if mouse is NOT pressed in a response field
            if mouseResponse.isPressedIn(square16, buttons=[0]):
                continue
            if mouseResponse.isPressedIn(square17, buttons=[0]):
                continue
            if mouseResponse.isPressedIn(square18, buttons=[0]):
                continue
            if mouseResponse.isPressedIn(square19, buttons=[0]):
                continue
                
            # record which response field is clicked
            for n, shape in enumerate(responseFields):
                if mouseResponse.isPressedIn(shape, buttons=[0]):
                    currentResponse = categoryLables[n] # save current response
                    handBrake = False # response is given so loosen the handbrake
                    
            # move to the next trial if the left mouse button is pressed and the hand brake is loosened
            buttons = mouseResponse.getPressed()
            if buttons[0] != 0 and handBrake == False:
                mouseResponse.setVisible(visible=False) # make mouse invisible again - minimize distraction while target stimulus is presented
                break

        # calculate current accuracy

        trueResponse = correct_answers[trialsBlock] # get true response from the list with all correct answers

        # compare current with true response
        if currentResponse == trueResponse:
            correctBlock = correctBlock + 1
            correctTotal = correctTotal + 1
        
        trialsBlock = trialsBlock + 1
        trialsTotal = trialsTotal + 1

        accuracyBlock = correctBlock / (trialsBlock /1)
        accuracyTotal = correctTotal / (trialsTotal /1)

        # write datafile

        thisImage = str(images[trialsBlock-1]).split(sep="/")[-1] # splitting the image folder path to get image file name only

        rawData.write ("%s, %s, %s, %.4f, %s, %s, %s, %s, %s, %s, %s, %.4f, %.4f\n"%
        (expInfo['subj'], expInfo['session'], "pt", rt, currentResponse, trueResponse, expInfo['condition'], thisImage, expInfo['age'],"practice", coverstory, accuracyBlock, accuracyTotal))
        

    # display a "Uuuups" message if practice trial criteria is not met and the child is older than 6
    if correctBlock <=8 and limit > 1: 

        while True:
        
            mouseTryAgain = event.Mouse(visible=False,win=win) # create mouse to grab rt when clicked
            tryAgain.draw()
            win.flip()

            theseKeys = event.getKeys(keyList=['escape'])
            if len(theseKeys) > 0:
                win.close()
                core.quit()

            # check for response
            buttons = mouseReaction.getPressed()
            if buttons[0] != 0:
                break

# calculate scores

thisStarScore = math.floor((len(range(correctBlock))/2))  # the star score of the current block is equal to half the correct responses (floored)
totStarScore = thisStarScore # in this first block the total star score is equal to the star score in this block cause it's the first


totCoinScore = 0 # set up a variable to store total coin score
thisCoinScore = 0 # set up a variable to store coin score for current block
thisCoinScore = thisCoinScore + 10 # initialize coin score
totCoinScore = totCoinScore + thisCoinScore # calculate new total coin score

totSpecialScore = 0 # set up a variable to store total special score
thisSpecialScore = 0 # set up a variable to store special score for current block
if correctBlock >= 9: # add 1 to special score if a certain performance is reached
    thisSpecialScore = thisSpecialScore + 1
    totSpecialScore = totSpecialScore + thisSpecialScore


# display scores

mouseScore = event.Mouse(visible=True,win=win)

thisCoinScoreDisp = visual.TextStim (win, text="X"+str(thisCoinScore), height = 90, pos = (130,50,)) # text for coin score of current block
thisSpecialScoreDisp = visual.TextStim (win, text="X"+str(thisSpecialScore), height = 90, pos = (130,-100)) # text for special score of current block
totScoreDisp = visual.TextStim (win, text="Total: " +str(totCoinScore) + "X         & " + str(totStarScore) +"X          & " + str(totSpecialScore) + "X", height = 30, pos = (-90,-240))

while True:

    frameScore.draw()
    coin1.draw()

    # draw empty stars and stars relative to performance
    for i in range(5):
        empty_stars[i].draw()
    for i in range(thisStarScore):
        stars[i].draw()
    
    emblem1.draw()
    thisCoinScoreDisp.draw()
    thisSpecialScoreDisp.draw()
    coin2.draw()
    star2.draw()
    emblem2.draw()
    totScoreDisp.draw()
    win.flip()

    buttons = mouseScore.getPressed()
    if buttons[0] != 0:
        break


# CONDITION EXAMPLE
#--------------------------------------------------------------------------#

if expInfo['condition'] == "snp":
    examplePath = PATH_SNP_EX
elif expInfo['condition'] == "eid":
    examplePath = PATH_EID_EX
elif expInfo['condition'] == "cc":
    examplePath = PATH_CC_EX

exampleStim = visual.ImageStim(win, size = 224, image=examplePath)

mouseExammple = event.Mouse(visible=False,win=win)

while True:

    exampleStim.draw()
    win.flip()


    # check for response
    buttons = mouseExammple.getPressed()
    if buttons[0] != 0:
        break

# TEST TRIALS
#--------------------------------------------------------------------------#

# get paths of meta blocks and also get the blockcount file (as data frame and as dictionary) according to condition

if expInfo['condition'] == 'snp':
    metablockPaths = os.listdir(PATH_METABLOCKS_SNP)
    metablockPaths = sorted([PATH_METABLOCKS_SNP + x for x in metablockPaths])
    PATH_BLOCK_COUNT = CWD_1UP+"/helper_files/block_counts/blockcount_snp_"+ageGroup+".csv"
    blockCount = pd.read_csv(PATH_BLOCK_COUNT)
    with open(PATH_BLOCK_COUNT, mode='r') as infile:
        reader = csv.reader(infile)
        with open('coors_new.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            blockCountDict = {rows[0]:rows[1] for rows in reader}
            blockCountDict.pop("block")
elif expInfo['condition'] == 'eid':
    metablockPaths = os.listdir(PATH_METABLOCKS_EID)
    metablockPaths = sorted([PATH_METABLOCKS_EID + x for x in metablockPaths])
    PATH_BLOCK_COUNT = CWD_1UP+"/helper_files/block_counts/blockcount_eid_"+ageGroup+".csv"
    blockCount = pd.read_csv(PATH_BLOCK_COUNT)
    with open(PATH_BLOCK_COUNT, mode='r') as infile:
        reader = csv.reader(infile)
        with open('coors_new.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            blockCountDict = {rows[0]:rows[1] for rows in reader}
            blockCountDict.pop("block")
elif expInfo['condition'] == 'cc':
    metablockPaths = os.listdir(PATH_METABLOCKS_CC)
    metablockPaths = sorted([PATH_METABLOCKS_CC + x for x in metablockPaths])
    PATH_BLOCK_COUNT = CWD_1UP+"/helper_files/block_counts/blockcount_cc_"+ageGroup+".csv"
    blockCount = pd.read_csv(PATH_BLOCK_COUNT)
    with open(PATH_BLOCK_COUNT, mode='r') as infile:
        reader = csv.reader(infile)
        with open('coors_new.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            blockCountDict = {rows[0]:rows[1] for rows in reader}
            blockCountDict.pop("block")

# create lists for each metablock containing a number of how often each block in this metablock has been completed

metablock1 = (blockCount['count'].values.tolist())[0:4]
metablock2 = (blockCount['count'].values.tolist())[4:8]
metablock3 = (blockCount['count'].values.tolist())[8:12]

metablocks = [metablock1,metablock2,metablock3]

# adjust if there are 5 metablocks as in the cue conflict condition.

if len(blockCount['count'].values.tolist()) > 16:
    metablock4 = (blockCount['count'].values.tolist())[12:16]
    metablock5 = (blockCount['count'].values.tolist())[16:]
    metablocks.append(metablock4)
    metablocks.append(metablock5)
else:
    metablock4 = (blockCount['count'].values.tolist())[12:]
    metablocks.append(metablock4)

# change the order of metablocks if each block in a metablock has has been completed x times. set this number by changing (i/x)

counter = 0

if metablock1[0] != 0:
    for i in metablock1: 
        if (i/7) >= 1:
            counter += 1
if counter == 4:
    metablockPaths += [metablockPaths.pop(0)]
    if metablock2[0] != 0:
        for i in metablock2:
            if (i/7) >= 1:
                counter += 1
if counter == 8:
    metablockPaths += [metablockPaths.pop(0)]
    if metablock3[0] != 0:
        for i in metablock3:
            if (i/7) >= 1:
                counter += 1
if counter == 12:
    metablockPaths += [metablockPaths.pop(0)]
    if metablock4[0] != 0:
        for i in metablock4:
            if (i/7) >= 1:
                counter += 1
if counter == 16:
    metablockPaths += [metablockPaths.pop(0)]
    if expInfo['condition'] == 'cc':
        if metablock5[0] != 0:
            for i in metablock5:
                if (i/7) >= 1:
                    counter += 1
    else:
        # save full block count list if condition is eid or snp
        blockCount.to_csv((CWD_1UP+"/helper_files/block_counts/full/"+ expInfo['condition'] + "_" + ageGroup + "_" + expInfo['subj'] + ".csv"), index = False)
        # reset block count list if condition is eid or snp
        blockCount.loc[:, 'count'] = 0
if counter == 20:
    metablockPaths += [metablockPaths.pop(0)]
    # save full block count list if condition is cc
    blockCount.to_csv((CWD_1UP+"/helper_files/block_counts/full/"+ expInfo['condition'] + "_" + ageGroup + "_" + expInfo['subj'] + ".csv"), index = False)
    # reset block count list ifcondition is cc
    blockCount.loc[:, 'count'] = 0

blockCountList = blockCount['count'].values.tolist()

block = 1 # creates a variable to store block number

trialsTotal = 0 # track number of total test trials 
correctTotal = 0 # track number of total correct test trials


for metaBlockPath in metablockPaths:

    # make a list of all paths in current metablock
    blockPaths = os.listdir(metaBlockPath)
    blockPaths = [metaBlockPath + "/" + x for x in blockPaths]

    # get number of current metablock
    numbMetablock = int((metaBlockPath.split("/")[-1]).split("_")[-1])

    # make a dictionary for the current metablock containing the number of how many times the blocks in this metablock have been completed
    if numbMetablock == 1:
        wantedKeys =['block_1','block_2','block_3','block_4']
        metaBlockDict = {x:blockCountDict[x] for x in wantedKeys}
        metaBlockDict = {k: v for k, v in sorted(metaBlockDict.items(), key=lambda item: item[1])}
    elif numbMetablock == 2:
        wantedKeys =['block_5','block_6','block_7','block_8']
        metaBlockDict = {x:blockCountDict[x] for x in wantedKeys}
        metaBlockDict = {k: v for k, v in sorted(metaBlockDict.items(), key=lambda item: item[1])}
    elif numbMetablock == 3:
        wantedKeys =['block_9','block_10','block_11','block_12']
        metaBlockDict = {x:blockCountDict[x] for x in wantedKeys}
        metaBlockDict = {k: v for k, v in sorted(metaBlockDict.items(), key=lambda item: item[1])}
    elif numbMetablock == 4:
        wantedKeys =['block_13','block_14','block_15','block_16']
        metaBlockDict = {x:blockCountDict[x] for x in wantedKeys}
        metaBlockDict = {k: v for k, v in sorted(metaBlockDict.items(), key=lambda item: item[1])}
    elif numbMetablock == 5:
        wantedKeys =['block_17','block_18','block_19','block_20']
        metaBlockDict = {x:blockCountDict[x] for x in wantedKeys}
        metaBlockDict = {k: v for k, v in sorted(metaBlockDict.items(), key=lambda item: item[1])}

    # sort the path list of blocks in this metablock. blocks which have been completed least comes first
    for k in metaBlockDict.keys():
        for blockPath in blockPaths:
            if k.split("_")[-1] == (blockPath.split("/")[-1]).split("_")[-1]:
                blockPaths.remove(blockPath)
                blockPaths.append(blockPath)

    for blockPath in blockPaths: # outer loop: iterates through the folders in the metafolders. each such folder contains the 20
                                        # stimuli of one block (one condition only)
        
        whichBlock = int((blockPath.split("/")[-1]).split("_")[-1]) # gets the block number
        
        # creates a file list with stimuli paths, which can be used later on to iterate through the stimuli
        images = []
        for imageName in os.listdir(blockPath):
                images.append(blockPath + "/" + imageName)

        # get difficulty levels

        diffLow = []
        others = []
        
        # sort image list according to difficulty levels (3 easy at the begining and 3 easy at the end of block)

        # get the difficulty levels for the different conditions
        if expInfo['condition'] == 'snp':
            for image in images:
                diffLevel = (image.split("/")[-1]).split("_")[1]
                if float(diffLevel) <= 0.1:
                    diffLow.append(image)
                elif float(diffLevel) > 0.1:
                    others.append(image)
        elif expInfo['condition'] == 'eid':
            for image in images:
                diffLevel = (image.split("/")[-1]).split("_")[1]
                if float(diffLevel) <= 4:
                    diffLow.append(image)
                elif float(diffLevel) > 4:
                    others.append(image)
        elif expInfo['condition'] == 'cc':
            for image in images:
                diffLevel = (image.split("/")[-1]).split("_")[1]
                if float(diffLevel) == 0:
                    diffLow.append(image)
                elif float(diffLevel) == 1:
                    others.append(image)
        
        images = [] # clear image list to be filled again in the right order

        # set a random seed which is individual with regard to current participant
        ran.seed()
        
        beginEnd = ran.sample(diffLow,6) # sample 6 element with low difficulty. 3 for the begining and 3 for the end

        # remove these images from the diffLow list and append the remanining images in this list back to the other images of this block
        for image in beginEnd:
            diffLow.remove(image)
        for image in diffLow:
            others.append(image)
        
        beginning = ran.sample(beginEnd,3) # sapmle 3 images for the beginning

        # add those three images at the begnning of the final image list of this block and remove them from the beginEnd list cause they're allready in place
        for image in beginning:
            images.append(image)
            beginEnd.remove(image)
        
        # randomly add the middle 14 images
        ran.shuffle(others)
        for image in others:
            images.append(image)
        
        # add the remanining 3 easy images at the end
        for image in beginEnd:
            images.append(image)

        # fill list with correct answers of current block
        correctAnswers = [] # reset list of correct answers for each block

        for image in images:
                correctAnswer = (image.split("/")[-1]).split("_")[2]
                correctAnswers.append(correctAnswer)

        # stimuli
        testClock=core.Clock() # creates a clock to meassure rt
        testStim = visual.ImageStim(win, size = 224, image= images[0]) 

        trialsBlock = 0 # track number of trials in this block
        correctBlock = 0 # track number of correct trials in this block

        testTrials = data.TrialHandler(nReps=1, method='sequential',
            extraInfo=expInfo,
            trialList=images,
            seed=None, name='testTrials')

        # add the loop to the experimentHandler // saves the conditions to the data
        thisExp.addLoop(testTrials)


        # "are you ready" screen

        while True:

            mouseReady = event.Mouse(visible=False,win=win)

            flags.draw()
            ready.draw()
            win.flip()

            # proceed when left click
            buttons = mouseReady.getPressed()
            if buttons[0] != 0:
                break
                

        # Start of inner Loop // iterates through the all stimuli of the current block
        for thisTrial in testTrials:

            # progress bar settings and progressbar stimuli 
            progress = (trialsBlock+1) * 40 # sets parameter for progress bar in response field
            prog_bar = visual.Rect(win, pos=((-400 + (progress/2)),-350), size=(progress,40), lineColor='White',fillColor="white", fillColorSpace='rgb')
            character = visual.ImageStim(win, pos = ((-400+progress), -350), size=80, image=PATH_CHARACTER)

            # fixation circle
            for n in range(9):
                for frameN in range(CIRCLE_DUR_SEQ):
                    circleFull.draw()
                    for i in range(n):
                        circleCounts[i-1].draw()
                    circleEmpty.draw()
                    win.flip()
            
            # target stimulus presentation 18 frames --> 300ms
            testStim.setImage(images[trialsBlock])

            for frameN in range(IMAGE_DUR):
                testStim.draw()
                win.flip()

            # white noise mask 18 frames -> 300ms    
            for frameN in range(MASK_DUR):
                noise.draw()
                win.flip()

            # get reaction time while children respond physically
            testClock.reset()
            while True:
                
                mouseReaction = event.Mouse(visible=False,win=win) # create mouse to grab rt when clicked

                win.flip()

                #enabling esc
                theseKeys = event.getKeys(keyList=['escape'])
                if len(theseKeys) > 0:
                    win.close()
                    core.quit()

                # check for response
                buttons = mouseReaction.getPressed()
                if buttons[0] != 0:
                    rt = testClock.getTime()
                    thisExp.addData('response.rt',rt)
                    break

            # response screen

            mouseResponse = event.Mouse(visible=True,win=win, newPos = [-300,0]) # create mouse to choose a certain category
            handBrake = True # apply the hand break to prevent loop from collapsing when the mouse ist clicked too fast in succesion


            # draw response surface 

            while True: 

                #draw non response fields
                for field in nonResponseFields:
                    field.draw()

                #draw repsonse field
                for field in responseFields:
                    field.draw()

                #draw response layout (icons)
                for icon in iconStimuli:
                    icon.draw()


                # progress bar
                prog_bar_outline.draw()
                prog_bar.draw()
                flagsSmall.draw()
                character.draw()
                win.flip()

                # continue if mouse is NOT pressed in a response field
                if mouseResponse.isPressedIn(square16, buttons=[0]):
                    continue
                if mouseResponse.isPressedIn(square17, buttons=[0]):
                    continue
                if mouseResponse.isPressedIn(square18, buttons=[0]):
                    continue
                if mouseResponse.isPressedIn(square19, buttons=[0]):
                    continue

                # enabling esc
                theseKeys = event.getKeys(keyList=['escape'])
                if len(theseKeys) > 0:
                    win.close()
                    core.quit()

                # record which response field is clicked
                for n, shape in enumerate(responseFields):
                    if mouseResponse.isPressedIn(shape, buttons=[0]):
                        thisExp.addData('response.field',categoryLables[n]) #stores data in output data file
                        currentResponse = categoryLables[n]
                        handBrake = False # response is given so loosen the handbrake

                
                # move to the next trial if the left mouse button is pressed and the handbrake is loosened
                buttons = mouseResponse.getPressed()
                if buttons[0] != 0 and handBrake == False:
                    mouseResponse.setVisible(visible=False) # make mouse invisible again - minimize distraction while target stimulus is presented
                    break

            # calculate current accuracy

            # get true reponse form the correct answers list
            trueResponse = correctAnswers[trialsBlock]

            # if the given response is equal to (part of for cc condition) the true response, increase the number of correct answers in this block by one
            if currentResponse in trueResponse:
                correctBlock = correctBlock + 1
                correctTotal = correctTotal + 1

            # increase trial per block and in total by one
            trialsBlock = trialsBlock + 1
            trialsTotal = trialsTotal + 1

            # calculate accuracy in the current block and for all answers given till now
            accuracyBlock = correctBlock / (trialsBlock / 1)
            accuracyTotal = correctTotal / (trialsTotal / 1)

            # make adjustments for the cc condition. if its a cc stimuli write the shape category as category in the data file.
            if len(trueResponse.split('-')) != 2:
                trueResponseForData = trueResponse
            else:
                trueResponseForData = (trueResponse.split('-')[0])
                trueResponseForData = ''.join([i for i in trueResponseForData if not i.isdigit()])

            # add stuff to the data file
            thisExp.addData("overall accuracy", round(accuracyTotal,4)) # adds the current overall accuracy (rounded)
            thisExp.addData("within block accuracy", round(accuracyBlock,4)) # adds the current withinblock accuracy (rounded)
            thisExp.addData('block', block) # add the current block to the data file
            thisExp.addData('coverstory', coverstory) # adds chosen coverstory to datafile
            thisExp.nextEntry() # creates new line in data file

            # write a row for current trial in rawData file

            # thisImage = images[trialsBlock]
            thisImage = str(images[trialsBlock-1]).split(sep="/")[-1] # splitting the image folder path to get image file name only

            rawData.write ("%s, %s, %s, %.4f, %s, %s, %s, %s, %s, %s, %s, %.4f, %.4f\n"%
            (expInfo['subj'], expInfo['session'], trialsTotal, rt, currentResponse, trueResponseForData, expInfo['condition'], thisImage, expInfo['age'],whichBlock, coverstory, accuracyBlock, accuracyTotal))
        
        # preparation for next block

        block = block + 1 # increase block counter by one ( count blocks current participant has finished)

        blockCountList[whichBlock-1] = blockCountList[whichBlock-1] + 1 # count how many times blocks are presented to a participant

        blockCount['count'] = blockCountList # refresh column in dataframe
        blockCount.to_csv(PATH_BLOCK_COUNT, index = False) # safe list to csv file for next participant
        
        # calculate scores

        thisStarScore = math.floor((len(range(correctBlock))/2)) + starBonus
        if thisStarScore > 10:
            thisStarScore = 10
        totStarScore = totStarScore + thisStarScore # calculate new total star score

        
        thisCoinScore = 0 # set up a variable to store coin score for current block
        thisCoinScore = thisCoinScore + 10 # initialize coin score
        totCoinScore = totCoinScore + thisCoinScore # calculate new total coin score

        thisSpecialScore = 0 # set up a variable to store special score for current block
        if thisStarScore >= 9: # add 1 to special score if a certain performance is reached
            thisSpecialScore = thisSpecialScore + 1
            totSpecialScore = totSpecialScore + thisSpecialScore

        # display scores

        mouseScore = event.Mouse(visible=False,win=win)

        thisCoinScoreDisp = visual.TextStim (win, text="X"+str(thisCoinScore), height = 90, pos = (130,50,)) # text for coin score of current block
        thisSpecialScoreDisp = visual.TextStim (win, text="X"+str(thisSpecialScore), height = 90, pos = (130,-100)) # text for special score of current block
        totScoreDisp = visual.TextStim (win, text="Total: " +str(totCoinScore) + "X         & " + str(totStarScore) +"X          & " + str(totSpecialScore) + "X", height = 30, pos = (-90,-240))

        while True:

            frameScore.draw()
            coin1.draw()

            # draw empty stars and stars relative to performance
            for emptyStar in empty_stars:
                emptyStar.draw()
            for i in range(thisStarScore):
                stars[i].draw()

            emblem1.draw()
            thisCoinScoreDisp.draw()
            thisSpecialScoreDisp.draw()
            coin2.draw()
            star2.draw()
            emblem2.draw()
            totScoreDisp.draw()
            win.flip()

            buttons = mouseScore.getPressed()
            if buttons[0] != 0:
                break


core.quit()
