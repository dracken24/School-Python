from raylib import *
from pyray import Font
from button import MyButton

WINDOW_WIDTH: int = 293;
WINDOW_HEIGHT: int = 440;
WINDOW_TITLE: str = "Calculatator";
FONT_COLOR = DARKGRAY;

font = GetFontDefault();

def init_font():
# {
    global font;
    try:
    #{
        # Try load a custom font
        custom_font = LoadFont("../assets/HighlandGothicFLF.ttf".encode('utf-8'));
        if custom_font and custom_font.texture.id > 0:
        #{
            font = custom_font;
            print("Font charged");
        #}
        else:
        #{
            # if error load font, use default font
            font = GetFontDefault();
            print("Use défaut font");
        #}
        
        # Define size if is font 0
        if font.baseSize == 0:
        #{
            font.baseSize = 32;
        #}
            
        print(f"Font loaded: {font.texture.id > 0}");
        print(f"Font base size: {font.baseSize}");
    #}
    except Exception as e:
    #{
        print(f"Error when loading font: {e}");
        print("Use défaut font");
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

def calculation(textAffich: str) -> bool:
# {
    # print("Execute: ", textAffich);
    try:
    # {
        # execute
        result = eval(textAffich);

        change_affich_text(str(result));
        return True;
    # }
    except Exception as exeption:
    # {
        print(f"Error: {exeption}");
        return False;
    # }
# }
