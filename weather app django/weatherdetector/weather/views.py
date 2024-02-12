from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':  # Corrected the request method check
        city = request.POST.get('city', '')  # Use request.POST.get to avoid KeyErrors
        api_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=cb771e45ac79a4e8e2205c0ce66ff633'.format(city)
        
        try:
            res = urllib.request.urlopen(api_url).read().decode('utf-8')  # Corrected the URL construction
            json_data = json.loads(res)
            data = {
                "country_code": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']) + ', ' + str(json_data['coord']['lat']),
                "temp": str(json_data['main']['temp']) + 'K',
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity']),
            }
        except urllib.error.HTTPError as e:
            # Handle HTTP errors, for example, if the city is not found
            data = {"error": "City not found"}
    else:
        city = ''
        data = {}

    return render(request, 'index.html', {'city': city, 'data': data})

