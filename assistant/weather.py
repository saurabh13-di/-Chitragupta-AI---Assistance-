import requests
def get_weather(city):
    if not city.strip(): raise ValueError('Use: weather in <city>')
    headers={'User-Agent':'ChitraguptaAI-StudentProject/1.0'}
    g=requests.get('https://geocoding-api.open-meteo.com/v1/search',params={'name':city,'count':1,'language':'en','format':'json'},headers=headers,timeout=10); g.raise_for_status()
    results=g.json().get('results',[])
    if not results: return f"City '{city}' not found. Check spelling."
    p=results[0]
    r=requests.get('https://api.open-meteo.com/v1/forecast',params={'latitude':p['latitude'],'longitude':p['longitude'],'current':'temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m','timezone':'auto'},headers=headers,timeout=10); r.raise_for_status()
    c=r.json().get('current',{}); codes={0:'Clear sky',1:'Mainly clear',2:'Partly cloudy',3:'Overcast',45:'Fog',48:'Fog',51:'Light drizzle',53:'Drizzle',55:'Dense drizzle',61:'Light rain',63:'Moderate rain',65:'Heavy rain',71:'Light snow',73:'Snow',75:'Heavy snow',80:'Rain showers',81:'Rain showers',82:'Heavy rain showers',95:'Thunderstorm',96:'Thunderstorm with hail',99:'Thunderstorm with hail'}
    return f"Weather in {p['name']}, {p.get('country','')}: {codes.get(c.get('weather_code'),'Current conditions')}. Temperature {c.get('temperature_2m','N/A')}°C, feels like {c.get('apparent_temperature','N/A')}°C, humidity {c.get('relative_humidity_2m','N/A')}%, wind {c.get('wind_speed_10m','N/A')} km/h."
