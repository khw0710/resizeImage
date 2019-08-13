import cv2
import glob
import os
import argparse
from pathlib import Path

def main( args ):
    input_dir = Path( args.input_dir )
    assert input_dir.is_dir()
    print (input_dir)


    os.chdir(Path(input_dir))
    imgs = glob.glob('*.jpg')
    imgs.extend(glob.glob('*.jpeg'))
        
    print('Found files:')
    print(imgs)
        
    width = 1600
    print('Resizing all images be %d pixels wide' % width)
    
    folder = 'resized'
    if not os.path.exists(folder):
        os.makedirs(folder)
    for img in imgs:
        pic = cv2.imread(img, cv2.IMREAD_UNCHANGED)
        height = int(width * pic.shape[0] / pic.shape[1])
        pic = cv2.resize(pic, (width, height))
        cv2.imwrite(folder + '/' + img, pic)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument( "input_dir"  , type=str )
    main( parser.parse_args() )


