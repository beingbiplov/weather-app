from django.shortcuts import render, redirect
import requests

def index(request):
	#Provide openweather API KEY in the url below for this to work
	url ='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid= API_KEY_HERE'

	if request.method == "POST":
		try:
			r_city = request.POST.get('city_name')
			r= requests.get(url.format(r_city)).json()
			city_weather={
			'name': r['name'],
			'temperature':r['main']['temp'],
			'description':r['weather'][0]['description'],
			'icon': r['weather'][0]['icon'],
			'wind':r['wind']['speed']
		    }

			context = {'city_weather': city_weather}
			return render(request, 'weather/index.html', context)
		except KeyError:
			context={'msg': r_city + " doesnot exist in our database. Please try again  in following format: Manchester / Manchester, UK"}
			return render(request, 'weather/error.html', context)

		
	cities = ['New York', 'Manchester', 'Paris', 'Kathmandu']
	weather_data = []

	for city in cities:
		r= requests.get(url.format(city)).json()
		

		city_weather={
			'name': city,
			'temperature': r['main']['temp'],
			'description': r['weather'][0]['description'],
			'icon': r['weather'][0]['icon'],
			'wind': r['wind']['speed']
		}
		weather_data.append(city_weather)

	context = {'weather_data': weather_data}

	return render(request, 'weather/index.html', context)
