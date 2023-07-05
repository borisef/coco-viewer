import cocoviewer
import sys
import os

#images = '/home/borisef/data/vehicles/test'
jsn = '/home/borisef/data/vehicles/train/_annotations.coco.json'

print(sys.argv)

sys.argv = [sys.argv[0], '-i', os.path.dirname(jsn), '-a', jsn]


cocoviewer.main()
