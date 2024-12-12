from raylib import *
from pyray import Rectangle
from utility import *

# void  main(int argc, char **argv)
#{

    # Window init
InitWindow(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE.encode('utf-8'));
SetTargetFPS(60);  # FPS to 60

init_font();

textAffich: str = "0.00";
lastCharAffich: str = "";
firstNbrCt: bool = True;

change_affich_text(textAffich);

########################################################################

# Game loop
while (not WindowShouldClose()):    # Detect window close
#{
    # Drawing begin
    BeginDrawing();

    ClearBackground(LIGHTGRAY);     # Clear screen with white color

    # # Draw signs buttons */+- 1, 2, 3....
    tmpText: str = draw_all_buttons();

    if tmpText == "ENTER":
    # {
        if calculation(textAffich):
        # {
            # textAffich = "0.00";
            firstNbrCt = True;
            lastTextAffich = "";
        # }
        else:
        # {
            textAffich = "ERROR";
            firstNbrCt = True;
            lastTextAffich = "";
            change_affich_text(textAffich);
        # }
        continue
    # }
    
    # If user enter . for first char
    if tmpText and len(tmpText) > 0:
    # {
        if firstNbrCt == True:
        # {
            # print("Len: ", len(textAffich));
            if tmpText == '.':
            # {
                if firstNbrCt == True:
                # {
                    firstNbrCt = False;
                    textAffich = "";
                # }
                textAffich += '0';
            # }
        # }
        if len(textAffich) < 12:
        # {
            if len(textAffich) >= 0:
            # {
                if firstNbrCt == True and len(tmpText) > 0:
                # {
                    firstNbrCt = False;
                    textAffich = "";
                # }
            # }
            textAffich += tmpText;
            change_affich_text(textAffich);
            lastCharAffich = tmpText;
        # }
    # }

    # Draw Border
    DrawRectangleLinesEx(Rectangle(4, 4, WINDOW_WIDTH - 8, WINDOW_HEIGHT - 8), 4, DARKGRAY);

    EndDrawing();
#}

# Window close
CloseWindow();
#}
