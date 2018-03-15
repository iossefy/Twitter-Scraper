from bs4 import BeautifulSoup
from urllib.request import urlopen
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import requests
import sys
import os

def gui_show(image):
    plt.imshow(image, interpolation='nearest')
    plt.show()

def bad_request():
    print("Something went wrong!")
    print("Try to check your internet connection")
    print("or check if the user is valid.")
    sys.exit(1)

def banner():
    print("Welcome To Twitter Scraperrrrrr!")
    print("Usage: python scraper.py [twitter user]")
    sys.exit(0)

def resize(size, image):
    width, height = size
    image = image.resize(size, Image.ANTIALIAS)
    return image

try:
    user = sys.argv[1]
except Exception as e:
    banner()


if 'https://twitter.com/' not in user:
    source = requests.get('https://twitter.com/'+user)
else:
    source = request.get(user)

def twitter(uname):

    soup = BeautifulSoup(source.text, 'lxml')

    # Get Information
    title = soup.find('title').text
    try:

        username = soup.find('a', class_='ProfileHeaderCard-nameLink').text
    except Exception as e:
        bad_request()
    name_tag = soup.find('b', class_='u-linkComplex-target').text
    bio = soup.find('p', class_='ProfileHeaderCard-bio').text
    website = str(soup.find('span', class_='ProfileHeaderCard-urlText').text)
    website = website.replace(' ', '').replace('\n', '') # i am lazy so...

    # Get Image
    im_url = soup.find('img', class_='ProfileAvatar-image')['src']
    response = requests.get(im_url)
    img = Image.open(BytesIO(response.content))

    # TODO: Show Image In Terminal Window
    # Resize Image
    #img = resize((28, 28), img)

    # Save Image
    img.save(f'{user}.png', 'png')

    # Print To The Console
    print("\n-------------Console Output-------------")
    print(f"Title: {title}")
    print(f"Username: {username}")
    print(f"Name Tag: {name_tag}")
    print(f"\nBio: {bio}\n")
    print(f"Website: {website}")
    gui_show(img)

if __name__ == '__main__':
    twitter(user)
