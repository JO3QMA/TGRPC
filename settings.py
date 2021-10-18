class Settings:
  def __init__(self):
    self.img_width = 256
    self.img_height = 256
    self.img_bg_color = (0, 0, 0)
    self.img_margin = 8
    
    self.element_ary = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","ᛆ","ᛖ","ᚺ","ᛁ","ᚷ","ᚲ","ᛜ","ᚦ","ᛏ","ᛉ"]
    self.element_count = 40
    self.element_font_min_size = 1
    self.element_font_max_size = 32
    self.element_font_path = './fonts/RuneAMN_Sans_1.20171016.otf'
    self.element_font_color = (255, 255, 255)