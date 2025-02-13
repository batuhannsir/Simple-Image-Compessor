import os
import datetime

from jinja2.optimizer import optimize

try:
    from PIL import Image
except Exception as e:
    print("Please run 'pip install pillow' or 'pip3 install pillow'")
    exit()
def formatSize(byte):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if byte < 1024.0:
            return f"{byte:.2f} {unit}"
        byte /= 1024.0
dir = './'
target_dir = './compressed'

if not os.path.exists(target_dir):
    os.makedirs(target_dir)
    print(f"{target_dir} created.")
else:
    print(f"{target_dir} already exists.")

while True:
    optimizeStatus = input("Optimize images? (y/n): ")
    if optimizeStatus != "":
        if optimizeStatus == "y":
            optimizeStatus = True
            break
        elif optimizeStatus == "n":
            optimizeStatus = False
            break
while True:
    qualityVal = input("Quality of image? (0-100): ")
    if qualityVal != "":
        try:
            if int(qualityVal) >= 0 or int(qualityVal) <=100:
                qualityVal = int(qualityVal)
                break
        except Exception as e:
            print('Please enter your choise!')
while True:
    print(f'1 to JPG')
    print(f'2 to PNG')
    print(f'3 to GIF')
    print(f'4 to WEBP')
    formatChoise = input("Enter format number: ")
    if formatChoise != "":
        formats = ["","JPG","PNG","GIF","WEBP"]
        try:
            if int(formatChoise) > 0 and int(formatChoise) <=4:
                formatChoise = formats[int(formatChoise)]
                break
        except Exception as e:
            print('Please enter your choise!')
files = os.listdir(dir)
totalBefore = 0
totalAfter = 0
totalFile = 0
startAt = datetime.datetime.now()
forbiddenExtentions = [".jpg",".jpeg",".png",".gif",".bmp",".ico",".webp"]
for file in files:
    fileExtension = os.path.splitext(file)[1].lower()
    if fileExtension in forbiddenExtentions:
        beforeSize = os.path.getsize(dir+"/"+file)
        image = Image.open(dir+"/"+file)
        image.save(target_dir+"/"+file, formatChoise, optimize=optimizeStatus,quality=qualityVal)
        afterSize = os.path.getsize(target_dir+"/"+file)
        totalFile += 1
        totalBefore += beforeSize
        totalAfter += afterSize
        print(f'File: {file}, Before: {formatSize(beforeSize)}, After: {formatSize(afterSize)} - comperessed: {formatSize(beforeSize-afterSize)} - %{round((afterSize*100)/beforeSize,2)}')
    else:
        print(f'{file} - {fileExtension} is not supported')
print(f'Total compressed file: {totalFile}')
print(f'Total before size: {formatSize(totalBefore)}')
print(f'Total after size: {formatSize(totalAfter)}')
print(f'Total Compressed: {formatSize(totalBefore-totalAfter)}')
print(f'Spended Time: {datetime.datetime.now() - startAt}')
print('')
print('')
print(f'Compressed images send to {target_dir}')
print('')
print('')
print(f'End of the road')
print(f'Thanks for bthnsr9696@gmail.com')
print(f'Donate USDT TJyLFknYNqU5Uh72uNsbD95FbxCk9Lazzk')


