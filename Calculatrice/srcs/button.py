from raylib import *
from pyray import  Rectangle, Vector2, Color, Font

class MyButton: 
#{
    # Constructor
    def __init__(self, x: float, y: float, width: float, height: float,
                bgColor = GRAY, clickColor = WHITE, hoverColor = LIGHTGRAY,
                    text: str = "", font = GetFontDefault()) -> str:
    #{
        self.rect = Rectangle(x, y, width, height)
        self.bgColor = bgColor;
        self.clickColor = clickColor;
        self.hoverColor = hoverColor;
        self.is_clicked = False;
        self.text = text;
        self.text_color = BLACK;
    
        if font is None:
            self.font = GetFontDefault()
        else:
            self.font = font
            
        if self.font.baseSize == 0:
            self.font.baseSize = 32
    #}

    # Member Functions

    def draw_button(self, font_size: int = 0, spacing: int = 0,
                border_thick: int = 0, border_color = WHITE, skip_update: bool = False):
    #{
        text_pos = Vector2(self.rect.x + self.rect.width / 2, 
                        self.rect.y + self.rect.height / 2);

        if hasattr(self, 'text'):
        # {
            actual_size = font_size if font_size else self.font.baseSize;
            
            text_width = MeasureText(self.text.encode('utf-8'), actual_size);
            text_height = actual_size;

            text_pos = Vector2(
                self.rect.x + (self.rect.width - text_width) / 2,
                self.rect.y + (self.rect.height - text_height) / 2
            );
        # }

        if CheckCollisionPointRec(GetMousePosition(), self.rect) and not skip_update:
        #{
            if IsMouseButtonDown(MOUSE_BUTTON_LEFT):
            #{
                if hasattr(self, 'texture_click') and self.texture_click.id > 0:
                #{
                    DrawTextureEx(self.texture_click, Vector2(self.rect.x, self.rect.y),
                        0, self.scale, WHITE);
                #}
                else:
                #{
                    DrawRectangleRec(self.rect, self.clickColor);
                    if hasattr(self, 'text') and hasattr(self, 'font'):
                    #{
                        DrawTextEx(self.font, self.text.encode('utf-8'), text_pos,
                                font_size if font_size else self.font.baseSize, spacing, self.text_color);
                    #}
                    if not self.is_clicked:
                    #{
                        print("Clicked on: ", self.text);
                        self.is_clicked = True;
                        return self.text;
                    #}
                #}

                DrawRectangleLinesEx(self.rect, border_thick, border_color);
                return;
            #}

            if IsMouseButtonReleased(MOUSE_BUTTON_LEFT):
            #{
                self.is_clicked = False;
            #}

            if hasattr(self, 'texture_hover') and self.texture_hover.id > 0:
            #{
                DrawTextureEx(self.texture_hover, 
                            Vector2(self.rect.x, self.rect.y), 0, self.scale, WHITE);
            #}
            else:
            #{
                DrawRectangleRec(self.rect, self.hoverColor);
                if hasattr(self, 'text') and hasattr(self, 'font'):
                #{
                    DrawTextEx(self.font, self.text.encode('utf-8'), text_pos,
                            font_size if font_size else self.font.baseSize, spacing, self.text_color);
                #}
            #}
        #}
        else:
        #{
            if hasattr(self, 'texture') and self.texture.id > 0:
            #{
                DrawTextureEx(self.texture, Vector2(self.rect.x, self.rect.y),
                    0, self.scale, WHITE);
            #}
            else:
            #{
                DrawRectangleRec(self.rect, self.bgColor);
                if hasattr(self, 'text') and hasattr(self, 'font'):
                #{
                    DrawTextEx(self.font, self.text.encode('utf-8'), text_pos,
                            font_size if font_size else self.font.baseSize, spacing, self.text_color);
                #}
            #}
        #}
    #}

########################################################################
                                # GET
########################################################################

    def get_text(self):
    #{
        return self.text;
    #}

########################################################################
                                # SET
########################################################################

    def set_bg_color(self, color):
    #{
        self.bgColor = color;
    #}

    def set_text(self, text: str):
    #{
        self.text = text;
    #}
#}
