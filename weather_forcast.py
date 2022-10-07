from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
def weather(city):	
	print(f"What forcast do you want for {city}")
	print("1) For now")
	print("2) For the day")
	print("3) For tomorrow")
	choice = int(input())
	if choice == 1:
		time = " now"
	elif choice == 2:
		time = " today"
	elif choice == 3:
		time = " tomorrow"
	city=city+" weather" + time
	print("Getting forcast data...")
	res=requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0. i635i39l2j0l4j46j690.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
	soup = BeautifulSoup(res.text,'html.parser')  
	
	#get the required information
	location =  soup.select('#wob_loc')[0].getText().strip()
	time =  soup.select('#wob_dts')[0].getText().strip()
	info = soup.select('#wob_dc')[0].getText().strip()
	weather = soup.select('#wob_tm')[0].getText().strip()
	precipitation = soup.select('#wob_pp')[0].getText().strip()
	humidity = soup.select('#wob_hm')[0].getText().strip()

	print("------------------------------------")
	print(f"This is the weather forcast for {city}")
	print(f'Time: {time}, location: {location}')
	print(f"Weather forcast")
	print(f"Information: {info}")
	print(f"Weather: {weather}, Humidity: {humidity}, Precipitation: {precipitation}")
	print("------------------------------------")


print("Welcome to Weather Looker.")
print("")
print("Enter location or press 'q' to leave")
city = input()
while city!='q':
	if city:
		weather(city)
		city = ''
		print("")

	else:
		print("that was an empty one")
	print("Enter location or press 'q' to leave")
	city = input()
if city == 'q':
	print("Thanks for using Weather Looker")