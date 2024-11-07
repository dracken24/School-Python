from raylib import *
from pyray import  Rectangle, Vector2, Color

class MyButton:
#{
    # Constructor
    def __init__(self, x: float, y: float, width: float, height: float,
                bgColor: Color = GRAY, clickColor: Color = WHITE, hoverColor: Color = LIGHTGRAY):
    #{
        self.rect = Rectangle(x, y, width, height)
        self.bgColor = bgColor;
        self.clickColor = clickColor;
        self.hoverColor = hoverColor;
    #}

    # Member Functions
    def set_bg_color(self, color: Color):
    #{
        self.bgColor = color;
    #}

    def draw_button(self, font_size: int = 0, spacing: int = 0,
                border_thick: int = 0, border_color: Color = WHITE, skip_update: bool = False):
    #{
        mouse_pos = GetMousePosition()
        text_pos = Vector2(self.rect.x + self.rect.width / 2, 
                        self.rect.y + self.rect.height / 2)

        if hasattr(self, 'text') and hasattr(self, 'font'):
        #{
            text_vec = MeasureTextEx(self.font, self.text, 
                                    font_size if font_size else self.font.baseSize, 
                                    spacing)
            text_pos.x -= text_vec.x / 2
            text_pos.y -= text_vec.y / 2
        #}

        if CheckCollisionPointRec(mouse_pos, self.rect) and not skip_update:
        #{
            if IsMouseButtonDown(MOUSE_BUTTON_LEFT):
            #{
                if hasattr(self, 'texture_click') and self.texture_click.id > 0:
                #{
                    DrawTextureEx(self.texture_click, 
                                Vector2(self.rect.x, self.rect.y),
                                0, self.scale, WHITE)
                #}
                else:
                #{
                    DrawRectangleRec(self.rect, self.clickColor)
                    if hasattr(self, 'text') and hasattr(self, 'font'):
                    #{
                        DrawTextEx(self.font, self.text, text_pos,
                                font_size if font_size else self.font.baseSize, 
                                spacing, self.text_color)
                    #}
                #}

                if hasattr(self, 'on_click_callback') and not self.is_clicked:
                #{
                    self.on_click_callback(self.user_data)
                    self.is_clicked = True
                #}

                DrawRectangleLinesEx(self.rect, border_thick, border_color)
                return

            if IsMouseButtonReleased(MOUSE_BUTTON_LEFT):
            #{
                self.is_clicked = False
            #}

            if hasattr(self, 'texture_hover') and self.texture_hover.id > 0:
            #{
                DrawTextureEx(self.texture_hover, 
                            Vector2(self.rect.x, self.rect.y),
                            0, self.scale, WHITE)
            #}
            else:
            #{
                DrawRectangleRec(self.rect, self.hoverColor)
                if hasattr(self, 'text') and hasattr(self, 'font'):
                #{
                    DrawTextEx(self.font, self.text, text_pos,
                            font_size if font_size else self.font.baseSize, 
                            spacing, self.text_color)
                #}
            #}
        #}
        else:
        #{
            if hasattr(self, 'texture') and self.texture.id > 0:
            #{
                DrawTextureEx(self.texture, 
                            Vector2(self.rect.x, self.rect.y),
                            0, self.scale, WHITE)
            #}
            else:
            #{
                DrawRectangleRec(self.rect, self.bgColor)
                if hasattr(self, 'text') and hasattr(self, 'font'):
                #{
                    DrawTextEx(self.font, self.text, text_pos,
                            font_size if font_size else self.font.baseSize, 
                            spacing, self.text_color)
                #}
            #}
        #}
    #}
#}
