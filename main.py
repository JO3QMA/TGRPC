import random
from PIL import Image, ImageDraw, ImageFont
from settings import Settings

class ImageCreator:
  def __init__(self):
    self.settings = Settings()

  def font_size_change(self):
    font_size = random.randrange(self.settings.element_font_min_size, self.settings.element_font_max_size)
    if font_size > self.settings.element_font_max_size / 2:
      font_size = random.randrange(self.settings.element_font_min_size, self.settings.element_font_max_size)
    self.str_font = ImageFont.truetype(self.settings.element_font_path, font_size)

  def font_pos_randomizer(self):
    font_pos_x_min = self.settings.img_margin
    font_pos_x_max = self.settings.img_width - self.settings.img_margin
    font_pos_y_min = self.settings.img_margin
    font_pos_y_max = self.settings.img_height - self.settings.img_margin
    font_pos_x = random.randrange(font_pos_x_min, font_pos_x_max)
    font_pos_y = random.randrange(font_pos_y_min, font_pos_y_max)
    self.str_pos = (font_pos_x, font_pos_y)

  def draw_background(self):
    img_size = (self.settings.img_width, self.settings.img_height)
    bg_color = self.settings.img_bg_color
    self.img = Image.new("RGB", img_size, bg_color)
    self.draw = ImageDraw.Draw(self.img)

  def sample_char(self):
    self.str_char = random.choice(self.settings.element_ary)

  def font_putter(self):
    self.draw.text(self.str_pos, self.str_char, font = self.str_font, fill = self.settings.element_font_color)

  def debug_print(self):
    print(f'POS: {self.str_pos}, CHAR: {self.str_char}')

  def main(self):
    self.draw_background()
    for i in range(self.settings.element_count):
      self.font_size_change()
      self.font_pos_randomizer()
      self.sample_char()
      self.debug_print()
      self.font_putter()
    self.img.save('./test.png')
    
if __name__ == '__main__':
  img = ImageCreator()
  img.main()
