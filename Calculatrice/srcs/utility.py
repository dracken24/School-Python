from raylib import *
from pyray import Font
from button import MyButton

WINDOW_WIDTH: int = 293;
WINDOW_HEIGHT: int = 380;
WINDOW_TITLE: int = "Calculatator";
FONT_COLOR = DARKGRAY;

font: Font = GetFontDefault();

def init_font():
# {
    global font
    try:
    #{
        # Essayer de charger la police personnalisée
        custom_font = LoadFont("../assets/HighlandGothicFLF.ttf".encode('utf-8'))
        if custom_font and custom_font.texture.id > 0:
            font = custom_font
            print("Police personnalisée chargée avec succès")
        else:
            # Si échec, utiliser la police par défaut
            font = GetFontDefault()
            print("Utilisation de la police par défaut")
        
        # Définir une taille de base si elle est à 0
        if font.baseSize == 0:
            font.baseSize = 20
            
        print(f"Font loaded: {font.texture.id > 0}")
        print(f"Font base size: {font.baseSize}")
    #}
    except Exception as e:
    #{
        print(f"Erreur lors du chargement de la police: {e}")
        print("Utilisation de la police par défaut")
        font = GetFontDefault()
        font.baseSize = 20
    #}
#}

affichage: MyButton = MyButton(15, 15, WINDOW_WIDTH - 30, 50);
affichage.set_bg_color(GRAY);
affichage.set_text("45.667");

############################# init buttons #############################
# Operation Buttons
addiButton: MyButton = MyButton(15, affichage.rect.height + (50 + 10), 50, 50, GRAY, LIME, FONT_COLOR, "+", font);
subsButton: MyButton = MyButton(15, affichage.rect.height + (50 + 10) * 2, 50, 50, GRAY, LIME, FONT_COLOR, "-", font);
multiButton: MyButton = MyButton(15, affichage.rect.height + (50 + 10) * 3, 50, 50, GRAY, LIME, FONT_COLOR, "*", font);
diviButton: MyButton = MyButton(15, affichage.rect.height + (50 + 10) * 4, 50, 50, GRAY, LIME, FONT_COLOR, "/", font);

# Numbers Buttons
oneButton: MyButton = MyButton(15 + 50 + 40, affichage.rect.height + (50 + 10), 50, 50, GRAY, LIME, FONT_COLOR, "1", font);
fourButton: MyButton = MyButton(15 + 50 + 40, affichage.rect.height + (50 + 10) * 2, 50, 50, GRAY, LIME, FONT_COLOR, "4", font);
sevenButton: MyButton = MyButton(15 + 50 + 40, affichage.rect.height + (50 + 10) * 3, 50, 50, GRAY, LIME, FONT_COLOR, "7", font);

twoButton: MyButton = MyButton(15 + (50 + 25) * 2, affichage.rect.height + (50 + 10), 50, 50, GRAY, LIME, FONT_COLOR, "2", font);
fiveButton: MyButton = MyButton(15 + (50 + 25) * 2, affichage.rect.height + (50 + 10) * 2, 50, 50, GRAY, LIME, FONT_COLOR, "5", font);
heighButton: MyButton = MyButton(15 + (50 + 25) * 2, affichage.rect.height + (50 + 10) * 3, 50, 50, GRAY, LIME, FONT_COLOR, "8", font);
zeroButton: MyButton = MyButton(15 + (50 + 25) * 2, affichage.rect.height + (50 + 10) * 4, 50, 50, GRAY, LIME, FONT_COLOR, "0", font);

threeButton: MyButton = MyButton(15 + (50 + 20) * 3, affichage.rect.height + (50 + 10), 50, 50, GRAY, LIME, FONT_COLOR, "3", font);
sixButton: MyButton = MyButton(15 + (50 + 20) * 3, affichage.rect.height + (50 + 10) * 2, 50, 50, GRAY, LIME, FONT_COLOR, "6", font);
nineButton: MyButton = MyButton(15 + (50 + 20) * 3, affichage.rect.height + (50 + 10) * 3, 50, 50, GRAY, LIME, FONT_COLOR, "9", font);

########################################################################

def draw_all_buttons():
# {
    # Writing space
    # DrawRectangleRec(affichage.rect, affichage.bgColor);
    affichage.draw_button(36, 1, 4, BLUE, True);

    # Draw signs buttons */+-
    addiButton.draw_button(36, 1, 4, BLUE);
    subsButton.draw_button(36, 1, 4, BLUE);
    multiButton.draw_button(36, 1, 4, BLUE);
    diviButton.draw_button(36, 1, 4, BLUE);

    # Draw Numbers Buttons
    oneButton.draw_button(36, 1, 4, BLUE);
    fourButton.draw_button(36, 1, 4, BLUE);
    sevenButton.draw_button(36, 1, 4, BLUE);

    twoButton.draw_button(36, 1, 4, BLUE);
    fiveButton.draw_button(36, 1, 4, BLUE);
    heighButton.draw_button(36, 1, 4, BLUE);
    zeroButton.draw_button(36, 1, 4, BLUE);

    threeButton.draw_button(36, 1, 4, BLUE);
    sixButton.draw_button(36, 1, 4, BLUE);
    nineButton.draw_button(36, 1, 4, BLUE);
# }
