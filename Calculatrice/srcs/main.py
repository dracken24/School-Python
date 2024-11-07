from raylib import *
from pyray import Vector2, Rectangle
from utility import PrintTest
from button import MyButton

# Initialisation
WINDOW_WIDTH: int = 350;
WINDOW_HEIGHT: int = 650;
WINDOW_TITLE: int = "Calculatator";

# void  main(int argc, char **argv)
#{
    # Window init
InitWindow(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE.encode('utf-8'));
SetTargetFPS(60);  # FPS to 60

############################# init buttons #############################

affichage: MyButton = MyButton(15, 15, WINDOW_WIDTH - 30, 50);
affichage.set_bg_color(GRAY)

addiButton: MyButton = MyButton(15, affichage.rect.height + (50 + 10), 50, 50, DARKGRAY, LIME, GRAY);
subsButton: MyButton = MyButton(15, affichage.rect.height + (50 + 10) * 2, 50, 50, DARKGRAY, LIME, GRAY);
multiButton: MyButton = MyButton(15, affichage.rect.height + (50 + 10) * 3, 50, 50, DARKGRAY, LIME, GRAY);
diviButton: MyButton = MyButton(15, affichage.rect.height + (50 + 10) * 4, 50, 50, DARKGRAY, LIME, GRAY);

########################################################################

# Game loop
while (not WindowShouldClose()):    # Detect window close
#{
    # Drawing begin
    BeginDrawing();

    ClearBackground(LIGHTGRAY);     # Clear screen with white color
    vec2_Pos = Vector2(WINDOW_WIDTH, WINDOW_HEIGHT);

    # Writing space
    DrawRectangleRec(affichage.rect, affichage.bgColor);
    
    # Draw signs buttons */+-
    addiButton.draw_button();
    subsButton.draw_button();
    multiButton.draw_button();
    diviButton.draw_button();

    # Draw Border
    DrawRectangleLinesEx(Rectangle(4, 4, WINDOW_WIDTH - 8, WINDOW_HEIGHT - 8), 4, DARKGRAY);

    EndDrawing();
#}

# Window close
CloseWindow();
#}
