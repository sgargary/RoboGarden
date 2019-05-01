# -*- coding: utf-8 -*-
"""
Created on Wed May  1 09:37:41 2019

@author: Sahar
"""

count = None
blue_team = None
red_team = None


blue_team = []
red_team = []
Robo.rotateRight() 
for count2 in range(9):
    Robo.stepForward() 
    if Robo.getCellColor() == 'red':
        red_team.append(Robo.getCellText())
    elif Robo.getCellColor() == 'blue':
        blue_team.append(Robo.getCellText() )
      Robo.rotateLeft() 
Robo.stepForward() 
# To Be Replaced
Robo.stepForward() 
Robo.setCellText((len(red_team))) 



