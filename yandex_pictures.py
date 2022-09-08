import requests
from bs4 import BeautifulSoup
import lxml
import os
import platform
import re

dt_now = 0

lord = []
lord1 = []

storage = input('search: ')
url = f'https://yandex.ru/images/search?from=tabbar&text={storage}'

OS = platform.system()

OS = OS.upper()

lib = input("all/No_all: ")

lib = lib.upper()

responce = requests.get(url).text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find("div", class_= 'serp-controller__content')
all_image = block.find_all("div", class_= 'serp-item__preview')

for image in all_image:
	image_link = image.find('a').get('href')
	image_link2 = image.find('img', class_ = 'serp-item__thumb justifier__thumb').get('src')

	if lib == 'NO_ALL':
		if OS == 'WINDOWS':
				try:
					golf = re.split('img_url=|&text', image_link)

					k = golf[1]

					p = k.replace('%3A', ':').replace(r'%2F', '/').replace('%25','%').replace('%28', '(').replace('%29', ')')

					image_bytes = requests.get(p).content

					with open(f'{dt_now}.jpg','wb') as file:
						file.write(image_bytes)

					os.system(f"{dt_now}.jpg")

					Y = input("save (YES/NO): ")

					Y = Y.upper()

					if Y == 'YES':
						os.system("taskkill /f /IM Microsoft.Photos.exe")

					elif Y == 'NO':
						os.system("taskkill /f /IM Microsoft.Photos.exe")
						os.system(f"del {dt_now}.jpg")

					else:
						pass

					dt_now = dt_now + 1

				except requests.exceptions.ConnectionError:
					url3 = f'http:{image_link2}'

					image_bytes = requests.get(url3).content

					with open(f'{dt_now}.jpg','wb') as file:
						file.write(image_bytes)

					os.system(f"{dt_now}.jpg")

					Y = input("save (YES/NO): ")

					Y = Y.upper()

					if Y == 'YES':
						os.system("taskkill /f /IM Microsoft.Photos.exe")

					elif Y == 'NO':
						os.system("taskkill /f /IM Microsoft.Photos.exe")
						os.system(f"del {dt_now}.jpg")

					else:
						pass

					dt_now = dt_now + 1

		elif OS == 'LINUX':
			try:
				golf = re.split('img_url=|&text', image_link)

				k = golf[1]

				p = k.replace('%3A', ':').replace(r'%2F', '/').replace('%25','%').replace('%28', '(').replace('%29', ')')

				image_bytes = requests.get(p).content

				with open(f'{dt_now}.jpg', 'wb') as file:
					file.write(image_bytes)

				os.system(f"{dt_now}.jpg")

				Y = input("save (YES/NO): ")

				Y = Y.upper()

				if Y == 'YES':
					pass

				elif Y == 'NO':
					os.system(f"rm -r {dt_now}.jpg")

				else:
					pass

				dt_now = dt_now + 1

			except requests.exceptions.ConnectionError:
				url3 = f'http:{image_link2}'

				image_bytes = requests.get(url3).content

				with open(f'{dt_now}.jpg','wb') as file:
					file.write(image_bytes)

				os.system(f"fim {dt_now}.jpg")

				Y = input("save (YES/NO): ")

				Y = Y.upper()

				if Y == 'YES':
					pass

				elif Y == 'NO':
					os.system(f"rm -r {dt_now}.jpg")

				else:
					pass

				dt_now = dt_now + 1

	if lib == 'ALL':
		if OS == 'WINDOWS':
			try:
				golf = re.split('img_url=|&text', image_link)

				k = golf[1]

				p = k.replace('%3A', ':').replace(r'%2F', '/').replace('%25','%').replace('%28', '(').replace('%29', ')')

				image_bytes = requests.get(p).content

				with open(f'{dt_now}.jpg','wb') as file:
					file.write(image_bytes)

				dt_now = dt_now + 1

			except requests.exceptions.ConnectionError:
				url3 = f'http:{image_link2}'

				image_bytes = requests.get(url3).content

				with open(f'{dt_now}.jpg','wb') as file:
					file.write(image_bytes)

				print("Picture",dt_now)

				dt_now = dt_now + 1

		elif OS == 'LINUX':
			try:
				golf = re.split('img_url=|&text', image_link)

				k = golf[1]

				p = k.replace('%3A', ':').replace(r'%2F', '/').replace('%25','%').replace('%28', '(').replace('%29', ')')

				image_bytes = requests.get(p).content

				with open(f'{dt_now}.jpg','wb') as file:
					file.write(image_bytes)

				dt_now = dt_now + 1

			except requests.exceptions.ConnectionError:
				url3 = f'http:{image_link2}'

				image_bytes = requests.get(url3).content

				with open(f'{dt_now}.jpg','wb') as file:
					file.write(image_bytes)

				print("Picture",dt_now)

				dt_now = dt_now + 1