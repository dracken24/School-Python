from raylib import *
from pyray import Font
from button import MyButton

WINDOW_WIDTH: int = 293;
WINDOW_HEIGHT: int = 440;
WINDOW_TITLE: int = "Calculatator";
FONT_COLOR = DARKGRAY;

font: Font = GetFontDefault();

def init_font():
# {
    global font;
    try:
    #{
        # Essayer de charger la police personnalisée
        custom_font = LoadFont("../assets/HighlandGothicFLF.ttf".encode('utf-8'));
        if custom_font and custom_font.texture.id > 0:
        #{
            font = custom_font;
            print("Police personnalisée chargée avec succès");
        #}
        else:
        #{
            # Si échec, utiliser la police par défaut
            font = GetFontDefault();
            print("Utilisation de la police par défaut");
        #}
        
        # Définir une taille de base si elle est à 0
        if font.baseSize == 0:
        #{
            font.baseSize = 32;
        #}
            
        print(f"Font loaded: {font.texture.id > 0}");
        print(f"Font base size: {font.baseSize}");
    #}
    except Exception as e:
    #{
        print(f"Erreur lors du chargement de la police: {e}");
        print("Utilisation de la police par défaut");
        font = GetFontDefault();
        font.baseSize = 32;
    #}
#}

affichage: MyButton = MyButton(15, 15, WINDOW_WIDTH - 30, 50);
affichage.set_bg_color(GRAY);

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

dotButton: MyButton = MyButton(15 + (50 + 20) * 3, affichage.rect.height + (50 + 10) * 4, 50, 50, GRAY, LIME, FONT_COLOR, ".", font);

enterButton: MyButton = MyButton(15, affichage.rect.height + (50 + 10) * 5 + 15, WINDOW_WIDTH - 30, 50, GRAY, LIME, FONT_COLOR, "ENTER", font);

########################################################################

def draw_all_buttons() -> str:
# {
    # Writing space
    returnText: str = "";
    text: str = affichage.draw_button(36, 1, 4, BLUE, True);
    if text and len(text) > 0:
        returnText = text;

    # Draw signs buttons */+-
    text = addiButton.draw_button(36, 1, 4, BLUE);
    if text and len(text) > 0:
        returnText = text;
    text = subsButton.draw_button(36, 1, 4, BLUE);
    if text and len(text) > 0:
        returnText = text;
    text = multiButton.draw_button(36, 1, 4, BLUE);
    if text and len(text) > 0:
        returnText = text;
    text = diviButton.draw_button(36, 1, 4, BLUE);
    if text and len(text) > 0:
        returnText = text;

    # Draw Numbers Buttons
    text = oneButton.draw_button(36, 1, 4, BLUE);
    if text and len(text) > 0:
        returnText = text;
    text = fourButton.draw_button(36, 1, 4, BLUE);
    if text and len(text) > 0:
        returnText = text;
    text = sevenButton.draw_button(36, 1, 4, BLUE);
    if text and len(text) > 0:
        returnText = text;

    text = twoButton.draw_button(36, 1, 4, BLUE);
    if text and len(text) > 0:
        returnText = text;
    text = fiveButton.draw_button(36, 1, 4, BLUE);
    if text and len(text) > 0:
        returnText = text;
    text = heighButton.draw_button(36, 1, 4, BLUE);
    if text and len(text) > 0:
        returnText = text;
    text = zeroButton.draw_button(36, 1, 4, BLUE);
    if text and len(text) > 0:
        returnText = text;

    text = threeButton.draw_button(36, 1, 4, BLUE);
    if text and len(text) > 0:
        returnText = text;
    text = sixButton.draw_button(36, 1, 4, BLUE);
    if text and len(text) > 0:
        returnText = text;
    text = nineButton.draw_button(36, 1, 4, BLUE);
    if text and len(text) > 0:
        returnText = text;

    text = dotButton.draw_button(36, 1, 4, BLUE);
    if text and len(text) > 0:
        returnText = text;
    
    text = enterButton.draw_button(36, 1, 4, BLUE);
    if text and len(text) > 0:
        returnText = text;

    return returnText;
# }

def change_affich_text(text: str):
# {
    affichage.text = text;
# }

def check_for_double(textAffich: str, cmd: str) -> bool:
# {
    print("In double: ", len(textAffich))
    if len(textAffich) == 0 and (cmd[0] == '+' or cmd[0] == '-' or cmd[0] == '*' or cmd[0] == '/'):
    # {
        return True;
    # } 
    for charr in textAffich:
    # {
        if charr == '+' or charr == '-' or charr == '*' or charr == '/':
        # {
            if cmd[0] == '+' or cmd[0] == '-' or cmd[0] == '*' or cmd[0] == '/':
                return True;
        # }
    # }

    return False;
# }

def calculation(textAffich: str) -> bool:
# {
    return True;
# }
