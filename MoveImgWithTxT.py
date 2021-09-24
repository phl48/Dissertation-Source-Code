import glob
import random
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--number", default=0, type=int, help="How many pair of number do you want to extract from dir")
parser.add_argument("--source", default='', type=str, help="Select your file directory source")
parser.add_argument("--destination", default='', type=str, help="Select your destination")
args = parser.parse_args()

# change directory to file locatrion
os.chdir(args.source)

txtFileInDir = glob.glob("*.txt")
randomFile = random.choices(txtFileInDir, k=args.number)

for f in randomFile:
  name = f.split(".txt")[0]  # get the file name
  type = ''
  if os.path.exists(name + '.jpg'):
    type = '.jpg'
  elif os.path.exists(name + '.jpeg'):
    type = '.jpeg'
  elif os.path.exists(name + '.png'):
      type = '.png'

  os.popen("mv %s %s %s" % (f, name + type, args.destination))
