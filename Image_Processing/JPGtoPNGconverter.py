from PIL import Image
import os

class JPGtoPNGconverter:
    def __init__(self, source_folder, target_folder):
        self.source_folder = source_folder
        self.target_folder = target_folder
    
    def convert(self):
        total_image = len(os.listdir(self.source_folder))
        print(f'source folder --> {self.source_folder} having total {total_image} images.')
        path, dirs, files = os.walk(self.source_folder).__next__()
        if not os.path.exists(self.target_folder):
            os.makedirs(self.target_folder)
        for img in files:
            Image.open(path+img).save(self.target_folder+img.split('.')[0]+'.png', 'png')
        #img = Image.open(path)
        #img.save(self.target_folder+files+'.png', 'png')

            
# create class object and call convert function..
image_converter = JPGtoPNGconverter('./images/', './pngImages/')
image_converter.convert()
        
    