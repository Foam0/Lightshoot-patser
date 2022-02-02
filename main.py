import io
import random
import PIL.Image as Image
import bs4
import requests
import time
alphabet='abcdefghijklmnopqrstuvwxyz1234567890'
bad_image=Image.open(r"C:\Users\Maple\PycharmProjects\pythonProject1\1642945451.0532541.png")
bad_image_txt=bad_image.tobytes()
cnt=0
def random_string(x):
    s=''
    for i in range(x):
        s+=alphabet[random.randint(0,len(alphabet)-1)]
    return s
while True:
    try:
        zzzz=random_string(6)
        x = requests.get(f"https://prnt.sc/{zzzz}", headers={'User-Agent': 'Chrome'})
        x = bs4.BeautifulSoup(x.content, 'html')
        img = x.find(name='img')
        ss = img['src']
        link = (img['src'])
        if link[0]=='/' or link=='invalid key':
            print("no screen shot on random link")
            continue
        newimg = requests.get(link, headers={'User-Agent': 'Chrome'})
        image = Image.open(io.BytesIO(newimg.content))
        image_txt=(image.tobytes())
        if image_txt==bad_image_txt:
            print("Bad_image")
            continue
        cnt+=1
        print("saved",cnt)
        Image.Image.save(image, f'D:\images/{time.time()}.png', 'png')
    except:
        print(f"https://prnt.sc/{zzzz}")
