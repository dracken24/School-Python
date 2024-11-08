from raylib import *
from pyray import Rectangle
from utility import draw_all_buttons, init_font, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE

# void  main(int argc, char **argv)
#{

    # Window init
InitWindow(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE.encode('utf-8'));
SetTargetFPS(60);  # FPS to 60

init_font();

########################################################################

# Game loop
while (not WindowShouldClose()):    # Detect window close
#{
    # Drawing begin
    BeginDrawing();

    ClearBackground(LIGHTGRAY);     # Clear screen with white color

    # # Draw signs buttons */+-
    draw_all_buttons();

    # Draw Border
    DrawRectangleLinesEx(Rectangle(4, 4, WINDOW_WIDTH - 8, WINDOW_HEIGHT - 8), 4, DARKGRAY);

    EndDrawing();
#}

# Window close
CloseWindow();
#}
