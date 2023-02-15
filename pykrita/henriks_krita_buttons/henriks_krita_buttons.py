# BBD's Krita Script Starter Feb 2018
from krita import DockWidget, DockWidgetFactory, DockWidgetFactoryBase
from PyQt5.QtWidgets import *
import sys
import pyautogui as p
from time import sleep
from threading import Thread
import os
firstLine = ' '

export = False

DOCKER_NAME = 'Ryans Configuration'
DOCKER_ID = 'henriks_buttons'



def write(streng):
    log = open('log.txt', 'w')
    log.truncate(0)
    log.close()
    log = open('log.txt', 'a')
    log.write(str(streng))
    log.close()

def refresh():
    with open("log.txt") as f:
        lines = f.read()
        global firstline
        firstline = lines.split('\n', 1)[0]

def getline():
    return firstline



class HenriksOnscreenKritaShortcutButtons(DockWidget):
    r = 0

    def undo(self):
        Krita.instance().action('edit_undo').trigger()

    def playAndpause(self):
        Krita.instance().action('toggle_playback').trigger()

    def redo(self):
        x = 0
        while x <= 7:
            if os.path.exists("/home/soft-dev/Pictures/frame000"+str(x)+".png"):
                os.remove("/home/soft-dev/Pictures/frame000"+str(x)+".png")
            x += 1
        Krita.instance().action('render_image_sequence_again').trigger()

    def onionskin(self):
        Krita.instance().action('toggle_onion_skin').trigger()

    def previous_frame(self):
        if self.r > 0:
            Krita.instance().action('previous_frame').trigger()
            self.r -= 1

    def next_frame(self):
        if self.r < 7:
            Krita.instance().action('next_frame').trigger()
            write("TH")
            self.r += 1

    def mirror_canvas(self):
        Krita.instance().action('view_toggledockers').trigger()

    def only_canvas(self):
        Krita.instance().action('view_show_canvas_only').trigger()

    def reset_canvas_rotation(self):
        Krita.instance().action('clear').trigger()

    def create_button(self, text, parentWidget, action):
        button = QPushButton(text, parentWidget)
        button.clicked.connect(action)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        return button

    def __init__(self):
        super().__init__()
        self.setWindowTitle(DOCKER_NAME)

        mainWidget = QWidget(self)
        self.setWidget(mainWidget)
        mainWidget.setLayout(QVBoxLayout())

        previousBrushButton = self.create_button("Play/Pause", mainWidget, self.playAndpause)
        mainWidget.layout().addWidget(previousBrushButton)

        undoButton = self.create_button("Undo", mainWidget, self.undo)
        mainWidget.layout().addWidget(undoButton)

        rotateContainer = QWidget(self)
        rotateContainer.setLayout(QHBoxLayout())

        mainWidget.layout().addWidget(rotateContainer)
        rotateLeftButton = self.create_button("L", rotateContainer, self.previous_frame)
        rotateRightButton = self.create_button("R", rotateContainer, self.next_frame)
        rotateContainer.layout().addWidget(rotateLeftButton)
        rotateContainer.layout().addWidget(rotateRightButton)

        redoButton = self.create_button("Export", mainWidget, self.redo)
        mainWidget.layout().addWidget(redoButton)

        resetCanvasContainer = QWidget(self)
        resetCanvasContainer.setLayout(QHBoxLayout())
        mainWidget.layout().addWidget(resetCanvasContainer)

        resetZoomButton = self.create_button("Toggle Overlay", mainWidget, self.onionskin)
        resetCanvasContainer.layout().addWidget(resetZoomButton)
        resetCanvasRotationButton = self.create_button("Reset", mainWidget, self.reset_canvas_rotation)
        resetCanvasContainer.layout().addWidget(resetCanvasRotationButton)

        canvasContainer = QWidget(self)
        canvasContainer.setLayout(QHBoxLayout())
        mainWidget.layout().addWidget(canvasContainer)
        mirrorCanvasButton = self.create_button("Toggle Docker View", canvasContainer, self.mirror_canvas)
        canvasContainer.layout().addWidget(mirrorCanvasButton)
        onlyCanvasButton = self.create_button("Only", canvasContainer, self.only_canvas)
        canvasContainer.layout().addWidget(onlyCanvasButton)

    def canvasChanged(self, canvas):
        pass


instance = Krita.instance()
dock_widget_factory = DockWidgetFactory(DOCKER_ID,
                                        DockWidgetFactoryBase.DockLeft,
                                        HenriksOnscreenKritaShortcutButtons)

instance.addDockWidgetFactory(dock_widget_factory)
