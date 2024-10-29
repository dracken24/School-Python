from raylib import *
from pyray import Vector2
from utility import PrintTest

# Initialisation
WINDOW_WIDTH = 350;
WINDOW_HEIGHT = 650;
WINDOW_TITLE = "Calculatator";

# Window init
InitWindow(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE.encode('utf-8'));
SetTargetFPS(60);  # FPS to 60

# Game loop
while (not WindowShouldClose()):    # Detect window close
    # Drawing begin
    BeginDrawing();
    
    ClearBackground(DARKGRAY);     # Clear screen with white color
    vec2_Pos = Vector2(WINDOW_WIDTH, WINDOW_HEIGHT);
    PrintTest(vec2_Pos);

    EndDrawing();

# Window close
CloseWindow();
