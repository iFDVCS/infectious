#Hi Omar, this is Scott parts, I hope you enjoy it.
#It doesn't work in the end but it is really close to, you'll have more explanations further !

import pygame, pygame.font, pygame.event, pygame.draw  # import modules
from pygame.locals import *
pygame.init()  # initialize the program

# Constantes
image_accueil = 'biohazard.jpg'  # background home
image_fond = 'biohazard.jpg'  # background
white = (255, 255, 255)  # define color white

# Opening of Pygame screen
fenetreL = 900  # width
fenetreH = 500  # height
fenetre = pygame.display.set_mode((fenetreL, fenetreH))  # run the screen with chose w and h

# Titre
pygame.display.set_caption('SIR/SIS Interpretation game')

# Definitions

# Here I chose to put all the definitions. I will only details the 1rst
# type (e.g text) each time and not every time


def Bienvenue(text):
    welcome = "Welcome in SIR/SIS Modelling Game"  # text we want to put
    welcome_pol = pygame.font.SysFont("brodway", 60, bold=False, italic=False)  # chose police (bold/italic or not)
    welcome_text = welcome_pol.render(welcome, 1, (white))  # association of text + color
    welcome_rect = welcome_text.get_rect()  # creates a square that contains the text
    welcome_rect.center = (fenetreL / 2, 40)  # center the square at the chosen position
    fenetre.blit(welcome_text, (welcome_rect))  # stick the text on the background (text, position)

    created_by = "Created by : Scott, Abdou and Benjamin"
    created_by_pol = pygame.font.SysFont("brodway", 25, bold=False, italic=False)
    created_by_text = created_by_pol.render(created_by, 1, (200,0,0))
    created_by_rect = created_by_text.get_rect()
    created_by_rect.center = (fenetreL / 2, 65)
    fenetre.blit(created_by_text, created_by_rect)

    space_start = "PRESS SPACE TO CONTINUE"
    space_start_pol = pygame.font.SysFont("brodway", 50, bold=False, italic=False)
    space_start_text = space_start_pol.render(space_start, 1, (white))
    space_start_rect = space_start_text.get_rect()
    space_start_rect.center = (fenetreL / 2, 400)
    fenetre.blit(space_start_text, space_start_rect)



def parameters(text):
    param = "Example (for scale) :"
    param_pol = pygame.font.SysFont("broadway", 40, bold=False, italic=False)
    param_text = param_pol.render(param, 1, (185, 150, 40))
    fenetre.blit(param_text, (590, 100))

    param3 = "Recovery rate (alpha) = 0.15"
    param3_pol = pygame.font.SysFont("broadway", 30, bold=False, italic=False)
    param3_text = param3_pol.render(param3, 1, (white))
    fenetre.blit(param3_text, (590, 140))

    param2 = "Average number of"
    param2_pol = pygame.font.SysFont("broadway", 30, bold=False, italic=False)
    param2_text = param2_pol.render(param2, 1, (white))
    fenetre.blit(param2_text, (590, 180))

    param2b = "transmission (beta) = 1.5"
    param2b_pol = pygame.font.SysFont("broadway", 30, bold=False, italic=False)
    param2b_text = param2b_pol.render(param2b, 1, (white))
    fenetre.blit(param2b_text, (590, 200))

    param4 = "Number of days = 50"
    param4_pol = pygame.font.SysFont("broadway", 30, bold=False, italic=False)
    param4_text = param4_pol.render(param4, 1, (white))
    fenetre.blit(param4_text, (590, 240))



def model_choix(text):
    choix_model = "Choose your model !"
    choix_model_pol = pygame.font.SysFont("broadway", 60, bold=False, italic=False)
    choix_model_text = choix_model_pol.render(choix_model, 1, (white))
    choix_model_rect = choix_model_text.get_rect()
    choix_model_rect.center = (fenetreL / 2, 50)
    fenetre.blit(choix_model_text, (choix_model_rect))

    modelsir = "SIR Model (press R)"
    modelsir_pol = pygame.font.SysFont("broadway", 50, bold=False, italic=False)
    modelsir_text = modelsir_pol.render(modelsir, 1, (white))
    modelsir_rect = modelsir_text.get_rect()
    modelsir_rect.center = (fenetreL / 2, 155)
    fenetre.blit(modelsir_text, (modelsir_rect))

    modelsis = "SIS Model (press S)"
    modelsis_pol = pygame.font.SysFont("broadway", 50, bold=False, italic=False)
    modelsis_text = modelsis_pol.render(modelsis, 1, (white))
    modelsis_rect = modelsis_text.get_rect()
    modelsis_rect.center = (fenetreL / 2, 235)
    fenetre.blit(modelsis_text, (modelsis_rect))

    back = "Press Esc to go back"
    back_pol = pygame.font.SysFont("broadway", 20, bold=False, italic=False)
    back_text = back_pol.render(back, 1, (white))
    back_rect = back_text.get_rect()
    back_rect.center = (fenetreL / 2, 275)
    fenetre.blit(back_text, (back_rect))



def sir(text):
    hiv = "Model : SIR ! Choose starting parameters"
    hiv_pol = pygame.font.SysFont("broadway", 60, bold=False, italic=False)
    hiv_text = hiv_pol.render(hiv, 1, (white))
    hiv_rect = hiv_text.get_rect()
    hiv_rect.center = (fenetreL / 2, 50)
    fenetre.blit(hiv_text, (hiv_rect))



def sis(text):
    ebola = "Model : SIS ! Choose starting parameters"
    ebola_pol = pygame.font.SysFont("broadway", 60, bold=False, italic=False)
    ebola_text = ebola_pol.render(ebola, 1, (white))
    ebola_rect = ebola_text.get_rect()
    ebola_rect.center = (fenetreL / 2, 50)
    fenetre.blit(ebola_text, (ebola_rect))



def get_key(): # this will return the key you push on your computer (for later)
    while 1: # infinite loop
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass

#All text done, the much harder part now

def display_box(fenetre, message):  # creates the box that contains a chosen text
    # It will print a message in a box and in the middle of the screen"

    fontobject = pygame.font.Font(None, 30)  # police
    pygame.draw.rect(fenetre, (white),  # draw a square on the screen with white color
                     ((fenetre.get_width() / 2) - 100,  # chose position
                      (fenetre.get_height() / 2) - 10,
                      204, 24), 1)

    if len(message) != 0:  # if there is a message
        fenetre.blit(fontobject.render(message, 1, white),  # stick it in white on the screen
                     ((fenetre.get_width() / 2) - 95, (fenetre.get_height() / 2) - 5))  # position where it's stick
    pygame.display.flip()  # refresh the screen to see the changes


def ask(fenetre, question):  # here we want to ask a question and the user has to write the answer
    #pygame.font.init() #initialize fond
    current_string = [] #create a list
    display_box(fenetre, question + ": " + "".join(current_string)) #put the box on the screen

    while 1:
        inkey = get_key()
        if inkey == K_BACKSPACE: #if you push backspace
            current_string = current_string[0:-1] #it will erase the last caracter of the list
        elif inkey == K_RETURN: #to enter the settings when you are done
            break
        elif inkey == K_ESCAPE:
            current_string.append("") #so it does "nothing"
        elif inkey <= 127: #127 means ~all the characters (alphabet + numerical + other charaters)
            current_string.append(chr(inkey)) #appends to the list the input character
        display_box(fenetre, question + ": " + "".join(current_string)) #put the list in the screen with ":" answer
    return "".join(current_string)



def av_num_transm(): #this is the function that contains everything
    beta = (ask(fenetre, "beta")) #when you press ENTER (return) it will assign x to the number you put
    print('beta = ', beta) #the aim is to set the variables into Bejamin's program
                     # to modelize the plots with chosen parameters


def recov_rate(): #same for another parameter
    alpha = (ask(fenetre, "alpha"))
    print('alpha = ', alpha)


def days():
    n_days = (ask(fenetre, "Nbr days"))
    print('Nb of days = ', n_days)



# PRINCIPAL LOOP
continuer = 1 #needed variables for loops
continuer_accueil = 1
continuer_choix_model = 0
continuer_SIR = 0
continuer_SIS = 0

while continuer:
    accueil = pygame.image.load(image_accueil).convert() #load the image on pygame
    fenetre.blit(accueil, (0, 0)) #blit = stick. So it sticks the image to the screen
    pygame.display.flip() #refresh
    #Now we have a screen with a chosen picture for the background

    while continuer_accueil:
        Bienvenue('text') #runs the function to put text "Bienvenue"
        pygame.display.flip()
        pygame.time.Clock().tick(30) #set 30 frame per second so the program is not too fast

        for event in pygame.event.get(): #event is like mouse movement/clic or keyboard or other stuff (e.g. Joystic)

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE: #if you push escape down
            # it will run the following things (or if you clic on the cross on the top left corner (QUIT)
                continuer = 0 #to stop the 1rst loop and so close the whole loop to close the game
                continuer_accueil = 0 #close the current loop
                pygame.quit() #quit pygame

            if event.type == KEYDOWN and event.key == K_SPACE: #if you push the spacebar, you go to the next loop
                continuer_accueil = 0
                continuer_choix_model= 1

    while continuer_choix_model:
        fenetre.blit(accueil, (0, 0)) #here i do again the sticking of the background to "erase" what was before
        model_choix('test2') #text
        pygame.display.flip()
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            if event.type == QUIT:
                continuer = 0
                continuer_choix_model = 0
                pygame.quit()

            if event.type == KEYDOWN and event.key == K_ESCAPE: #here escape doesn't close the game
                continuer_choix_model = 0 #it just return to the previous loop so the "home"
                continuer_accueil = 1 #(here called accueil, because i did all the code in french to help me)

            if event.type == KEYDOWN and event.key == K_r: #press R to go to SIR model
                continuer_choix_model = 0
                continuer_SIR = 1

            if event.type == KEYDOWN and event.key == K_s: #press S to go to SIS model
                continuer_choix_model= 0
                continuer_SIS = 1

#From now on, every single peace of code is good and everything is working good. You can access to the menu,
#navigate with the keyboard, come back to home screen with ESCAPE key, close the program with the cross on the
#top left corner. The text is writen where i wanted in the police/color i wanted.

#The next part is not working to i will explain what i wanted to do and why i failed :
    #I wanted to :
        # see on the screen : "alpha : " and that the user could write the number he wanted. => IT WORKS
        # when the user is done, he presses ENTER (return) and the number he wrote was assign to a variable
        # alpha, beta, nb of days => IT WORKS
        # when the last variable is entered (nb of days) the "window" where you enter the variable closes => NOT WORKING
        # After that, stick Benjamin's code by the command : from "name of his file" import *
        # stick at the end of my SIR/SIS loop the plotting command (without alpha, beta and nb days variable)
        # because it would be already assign by the user with my program => NOT WORKING, it says that 'variable'
        # is not definited, i don't know why.
    #Also i have a small problem i cannot fix : When i do backspace to erase (in case you do a mistake)
    #when you set the variable, it doesn't work. But it did when i tried outside of the program (in another python file)
    #Another weird thing is that when the "variable window" is open, you cannot close the program without forcing to quit
    #I couldn't fix it

    while continuer_SIR:  #SIR Model loop (again the same things, stick background and some text)
        fenetre.blit(accueil, (0, 0))
        sir('test3')
        parameters('test')

        for event in pygame.event.get(): #quit with the cress or return with escape to previous screen

            if event.type == QUIT:
                continuer = 0
                continuer_SIR = 0
                pygame.quit()

            if event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_SIR = 0
                continuer_choix_model = 1

        recov_rate() #set the function to write the alpha value you want
        pygame.display.flip()


        fenetre.blit(accueil, (0, 0))
        sir('test3')
        parameters('test') #erase all the background and put it again

        av_num_transm()  #set the function to write the beta value you want
        pygame.display.flip()


        fenetre.blit(accueil, (0, 0))
        sir('test3')
        parameters('test')

        days() #set the function to write the number of days you want
        pygame.display.flip()

        fenetre.blit(accueil, (0, 0))
        sir('test3')
        pygame.display.flip()

        pygame.time.Clock().tick(30)


    while continuer_SIS:  #Same thing for SIS
        fenetre.blit(accueil, (0, 0))
        sis('test3')
        parameters('test')

        for event in pygame.event.get():

            if event.type == QUIT:
                continuer = 0
                continuer_SIS = 0
                pygame.quit()

            if event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_SIS = 0
                continuer_choix_model = 1

        recov_rate()
        pygame.display.flip()


        fenetre.blit(accueil, (0, 0))
        sis('test3')
        parameters('test')

        av_num_transm()
        pygame.display.flip()


        fenetre.blit(accueil, (0, 0))
        sis('test3')
        parameters('test')

        days()
        pygame.display.flip()

        fenetre.blit(accueil, (0, 0))
        sis('test3')
        pygame.display.flip()

        pygame.time.Clock().tick(30)

#That's all ! Even if it's not working, i learnt a lot and did my best.
#Also i tried tkinder as you told me but i couldn't understand as easiely as pygame (which is already
#complicated)
#I wanted to do the "plotting part" with basemap as you said but impossible to install it on my computer.
#I used pycharm with python 3 to do it, maybe it's the reason. I don't know.

#Best
#Scott Picquerey