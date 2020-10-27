import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((397, 562))
#фон
rect(screen, (175, 221, 233), (0, 0, 397, 562)) #голубой фон

#gory
polygon(screen, (179, 179, 179), [(0,173), (47,56),
(83,136), (136,74),
(237,224), (309,69),
(333,86), (397, 19),
(397,332), (222,332),
(222, 282), (0,296) ])
polygon(screen, (0, 0, 0), [(0,173), (47,56),
(83,136), (136,74),
(237,224), (309,69),
(333,86), (397, 19),
(397,332), (222,332),
(222, 282), (0,296) ], 2)

#pole
polygon(screen, (170, 222, 135), [(0,296), (222, 282),
(222,332), (397,332),
(397,562), (0,562) ])
polygon(screen, (0, 0, 0), [(0,296), (222, 282),
(222,332), (397,332),
(397,562), (0,562) ], 1)

#kust
circle(screen, (113, 200, 55), (338, 464), 75)

#uhi
polygon(screen, (255, 255, 255), [(143,294), (135,273), (152,293) ])
polygon(screen, (255, 255, 255), [(153,294), (145,273), (162,293) ])

#telo
ellipse(screen, (255, 255, 255), (70, 345, 91, 38))
ellipse(screen, (255, 255, 255), (140, 298, 25, 64))
ellipse(screen, (255, 255, 255), (140, 285, 38, 19))

#nogi pered blij
ellipse(screen, (255, 255, 255), (140, 370, 14, 31))
ellipse(screen, (255, 255, 255), (140, 395, 14, 31))
ellipse(screen, (255, 255, 255), (143, 423, 14, 10))

#nogi pered dal
ellipse(screen, (255, 255, 255), (125, 360, 14, 31))
ellipse(screen, (255, 255, 255), (125, 385, 14, 31))
ellipse(screen, (255, 255, 255), (128, 413, 14, 10))

#nogi zad blij
ellipse(screen, (255, 255, 255), (95, 370, 14, 31))
ellipse(screen, (255, 255, 255), (95, 395, 14, 31))
ellipse(screen, (255, 255, 255), (98, 423, 14, 10))

#nogi pered dal
ellipse(screen, (255, 255, 255), (75, 360, 14, 31))
ellipse(screen, (255, 255, 255), (75, 385, 14, 31))
ellipse(screen, (255, 255, 255), (78, 413, 14, 10))

#glaz
circle(screen, (229, 128, 255), (157, 293), 7)
circle(screen, (0, 0, 0), (160, 293), 3)

#romashki
ellipse(screen, (255, 255, 255), (310, 470, 20, 10))
ellipse(screen, (190, 191, 188), (310, 470, 20, 10), 1)

ellipse(screen, (255, 255, 255), (300, 467, 20, 10))
ellipse(screen, (190, 191, 188), (300, 467, 20, 10), 1)

ellipse(screen, (255, 255, 255), (295, 470, 20, 10))
ellipse(screen, (190, 191, 188), (295, 470, 20, 10), 1)

ellipse(screen, (255, 255, 0), (300, 475, 20, 10))

ellipse(screen, (255, 255, 255), (310, 480, 20, 10))
ellipse(screen, (190, 191, 188), (310, 480, 20, 10), 1)

ellipse(screen, (255, 255, 255), (315, 475, 20, 10))
ellipse(screen, (190, 191, 188), (315, 475, 20, 10), 1)

ellipse(screen, (255, 255, 255), (285, 475, 20, 10))
ellipse(screen, (190, 191, 188), (285, 475, 20, 10), 1)

ellipse(screen, (255, 255, 255), (290, 480, 20, 10))
ellipse(screen, (190, 191, 188), (290, 480, 20, 10), 1)

ellipse(screen, (255, 255, 255), (300, 483, 20, 10))
ellipse(screen, (190, 191, 188), (300, 483, 20, 10), 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
  clock.tick(FPS)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      finished = True

pygame.quit()