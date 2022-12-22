
from asyncio import create_subprocess_exec
from arena import *

from YarnParser import *
from ColorPrinter import *

# ------------------------------------------ #
# ------------HELPER VARIABLES-------------- #
# ------------------------------------------ #

class ArenaDialogueBubbleGroup():
    def __init__(self, scene, npc, dialogue, line):
        self.scene = scene
        self.npc = npc
        self.dialogue = dialogue

        self.speechBubble = self.createSpeechBubble(line)
        self.buttons = self.createButtons(line)

        self.SPEECH_BUBBLE_COLOR = (0,0,0)
        self.SPEECH_TEXT_COLOR = (0,0,0)
        self.CHOICE_BUBBLE_COLOR = (0,0,0)
        self.CHOICE_TEXT_COLOR = (0,0,0)

        self.SPEECH_BUBBLE_POSITION = (0,0,0)
        self.CHOICE_BUBBLE_POSITION = (0,0,0)
        self.CHOICE_BUBBLE_Y_OFFSET = 2

    #customization functions   
    def setColors(self, speechBubbleColor, speechTextColor, choiceBubbleColor, choiceTextColor):

        self.SPEECH_BUBBLE_COLOR = speechBubbleColor
        self.SPEECH_TEXT_COLOR = speechBubbleColor
        self.CHOICE_BUBBLE_COLOR = choiceBubbleColor
        self.CHOICE_TEXT_COLOR = choiceTextColor

    def setPositionOffsets(self, speechBubblePosition, choiceBubblePosition, choiceBubbleOffsetY):
        self.SPEECH_BUBBLE_POSITION = speechBubblePosition
        self.CHOICE_BUBBLE_POSITION = choiceBubblePosition
        self.CHOICE_BUBBLE_OFFSET_Y = choiceBubbleOffsetY

    def runCommands(self, line):
        commands = line.commands
        return

    #functions to create chat bubble from current line (at parent position)
    def createSpeechBubble(self, line):
        speech = line.text
        
        speechBubble = Text(
            object_id=self.npc.object_id + "_speechBubble",
            text=speech,
            parent=self.npc,
            align="center",
            color=(200,200,200),
            position=(0,0.7,0),
            scale=(0.4,0.4,0.4),
        )

        self.scene.add_object(speechBubble) # add the box
        return speechBubble

    def createButtons(self, line):
        choices = line.choices
        self.buttons = []
        if(len(choices) > 0): 
            for c in range(len(choices)):                
                choiceButton = Button(self.scene, self.npc, self.npc.object_id + "_choiceButton_"+str(c), choices[c].text, self.onClickChoiceButton, 
                                      position = (0, 0.2 + c * 0.15, 0.5), color = (100,100,200), textColor = (200,200,200))

                self.buttons.append(choiceButton)
        else: 
            nextButton = Button(self.scene, self.npc, self.npc.object_id + "_nextButton", "[Next]", self.onClickNextButton, 
                                position = (0,0.2,0.6), color = (100,100,200), textColor = (200,200,200))
                
            self.buttons.append(nextButton)
        return self.buttons

    def createNewButtons(self, line):
        self.createSpeechBubble(line)
        self.createButtons(line)
        self.runCommands(line)

    def clearButtons(self):
        self.scene.delete_object(self.speechBubble)
      
        for button in self.buttons:
            self.scene.delete_object(button.box)
            self.scene.delete_object(button.text)
            
        self.buttons = []

        return

    # ------------------------------------------ #
    # ------------HELPER VARIABLES-------------- #
    # ------------------------------------------ #

    #functions to control choice button click behaviour
    def onClickChoiceButton(self, scene, evt, msg):
        if evt.type == "mousedown":
            print("Choice Button Pressed!")

            choiceButtonID = msg["object_id"]
            filterLen = len(self.npc.object_id + "_choiceButton_")

            choiceButtonNumber = int(choiceButtonID[filterLen:])
            choiceNodeName = self.dialogue.currentNode.lines[self.dialogue.currentNode.currentLineIndex].choices[choiceButtonNumber].node

            self.clearButtons()
            #get the current line represented by the selections
        
            self.dialogue.currentNode = self.dialogue.nodes[self.dialogue.getNodeIndexFromString(choiceNodeName)]
            self.dialogue.currentNode.currentLineIndex = 0
            self.createNewButtons(self.dialogue.currentNode.lines[self.dialogue.currentNode.currentLineIndex])
                
            #bubbles.createNewButtons( dialogue.currentNode.currentLine )

    #functions to control choice button click behaviour
    def onClickNextButton(self, scene, evt, msg):
        if evt.type == "mousedown":
            print("Next Button Pressed!")
            
            self.clearButtons()
            self.dialogue.currentNode.currentLineIndex = self.dialogue.currentNode.currentLineIndex + 1

            if(self.dialogue.currentNode.currentLineIndex <= len(self.dialogue.currentNode.lines)):
                self.createNewButtons(self.dialogue.currentNode.lines[self.dialogue.currentNode.currentLineIndex])


# ------------------------------------------ #
# --------------ARENA CLASSES--------------- #
# ------------------------------------------ #

class Button():
    def __init__(self, scene, npc, name, text, eventHandler, position, color, textColor):
        self.scene = scene
        self.npc = npc

        self.box = self.makeButtonBox(name, text, eventHandler, color, position, buttonTextColor=textColor)
        self.text = self.makeButtonText(self.box, name, text, buttonColor=textColor)

    def makeButtonText(self, button, buttonID, buttonText, buttonColor = (255,255,255), buttonPos = (0, 0, 0.5), buttonRot = (0,0,0), buttonScale = (0.5, 2, 1)):
        buttonText = Text(
            object_id=buttonID+"_text",
            text=buttonText,
            align="center",
                
            position=buttonPos,
            rotation=buttonRot,
            scale=buttonScale,

            color=buttonColor,

            parent = button,
            persist=True,
        )
        self.scene.add_object(buttonText)
        return buttonText

    def makeButtonBox(self, buttonID, buttonText, buttonHandler, buttonColor = (128,128,128), buttonPos = (0,0,0), buttonRot = (0,0,0), buttonScale = (0.4, 0.08, 0.04), buttonTextColor = (255,255,255)):
        button = Box(
            object_id=buttonID,

            position=buttonPos,
            rotation=buttonRot,
            scale=buttonScale,

            color=buttonColor,

            parent = self.npc,
            clickable=True,
            persist=True,
            evt_handler=buttonHandler,
        )
        self.scene.add_object(button)
        return button
    
