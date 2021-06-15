from models.models import Game


class MockDb: 
   def __init__(self):
       self.db = {
           "games": [Game("Bloodborne", "Bloodborne is an action role-playing game developed by FromSoftware and published by Sony Computer Entertainment, which released for the PlayStation 4 in March 2015. Bloodborne follows the player's character, a Hunter, through the decrepit Gothic, Victorian era–inspired city of Yharnam"  ,"../static/images/bloodborne-cover.jpg" ,"../static/images/bloodborne-banner.jpg", ["PS4"]),
            Game("The Legend of Zelda: Ocarina of Time", "The Legend of Zelda: Ocarina of Time is an action-adventure game developed and published by Nintendo for the Nintendo 64. It was released in Japan and North America in November 1998, and in PAL regions the following month. Ocarina of Time is the fifth game in The Legend of Zelda series, and the first with 3D graphics.","../static/images/zelda-cover.jpg" ,"../static/images/zelda-banner.jpg", ["N64", "3DS"]),
            Game("The Witcher 3: Wild Hunt", "The Witcher 3: Wild Hunt is an action role-playing game developed and published by Polish developer CD Projekt Red and is based on The Witcher series of fantasy novels written by Andrzej Sapkowski.", "../static/images/witcher-cover.jpg", "../static/images/witcher-banner.jpg", ["PS4", "XBOX ONE", "SWITCH", "PC"] )
           ]
       }
