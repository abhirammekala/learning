import requests

url = 'https://restcountries.eu/rest/v2/alpha/'
countries = {'Belgium': 'BE', 'Bulgaria': 'BG', 'Japan': 'JP', 'Jamaica': 'JM', 'Jordan': 'JO', 'Brazil': 'BR', 'Belarus': 'BY', 'Russian Federation': 'RU', 'Panama': 'PA', 'Romania': 'RO', 'Guatemala': 'GT', 'Greece': 'GR', 'Bahrain': 'BH', 'Georgia': 'GE', 'United Kingdom': 'GB', 'Oman': 'OM', 'Botswana': 'BW', 'Croatia': 'HR', 'Hungary': 'HU', 'Hong Kong': 'HK', 'Puerto Rico': 'PR', 'Portugal': 'PT', 'Paraguay': 'PY', 'Latvia': 'LV', 'Peru': 'PE', 'Philippines': 'PH', 'Poland': 'PL', 'Estonia': 'EE', 'Egypt': 'EG', 'South Africa': 'ZA', 'Ecuador': 'EC', 'Albania': 'AL', 'Zimbabwe': 'ZW', 'Spain': 'ES', 'Montenegro': 'ME', 'Uruguay': 'UY', 'Uzbekistan': 'UZ', 'Myanmar': 'MM', 'Macao': 'MO', 'United States': 'US', 'Malta': 'MT', 'Ukraine': 'UA', 'Mexico': 'MX', 'Austria': 'AT', 'France': 'FR', 'Morocco': 'MA', 'Finland': 'FI', 'Nicaragua': 'NI', 'Netherlands': 'NL', 'Norway': 'NO', 'Namibia': 'NA', 'Nigeria': 'NG', 'New Zealand': 'NZ', "Cote D'Ivoire": 'CI', 'Switzerland': 'CH', 'Colombia': 'CO', 'China': 'CN', 'Chile': 'CL', 'Canada': 'CA', 'Czech Republic': 'CZ', 'Cyprus': 'CY', 'Costa Rica': 'CR', 'Cuba': 'CU', 'Syrian Arab Republic': 'SY', 'Kyrgyzstan': 'KG', 'Cambodia': 'KH', 'El Salvador': 'SV', 'Slovakia': 'SK', 'Slovenia': 'SI', 'North Korea': 'KP', 'Kazakhstan': 'KZ', 'Saudi Arabia': 'SA', 'Singapore': 'SG', 'Sweden': 'SE', 'Dominican Republic': 'DO', 'Denmark': 'DK', 'Germany': 'DE', 'Algeria': 'DZ', 'Lebanon': 'LB', "Lao People's Democratic Republic": 'LA', 'Turkey': 'TR', 'Sri Lanka': 'LK', 'Tunisia': 'TN', 'Lithuania': 'LT', 'Thailand': 'TH', 'United Arab Emirates': 'AE', 'Andorra': 'AD', 'Iceland': 'IS', 'Iran': 'IR', 'Italy': 'IT', 'Vietnam': 'VN', 'Argentina': 'AR', 'Australia': 'AU', 'Israel': 'IL', 'India': 'IN', 'Azerbaijan': 'AZ', 'Ireland': 'IE', 'Indonesia': 'ID', 'Malaysia': 'MY', 'Qatar': 'QA', 'South Korea': 'KR', 'Greenland': 'GL', 'Palestine': 'PS', 'Holy See': 'VA', 'Taiwan': 'TW', 'Afghanistan': 'AF'}
more = "y"
while more == "y":
    country = input("country: ")
    if country in countries:
        code = countries[country]
        response = requests.get(url + code)
        if response:
            data = response.json()
            print("Name of country: ", data['name'])
            print("Capital: ", data['capital'])
            print("Demonym: ", data['demonym'])
    else:
        print("sorry we could not find your country :'( ")
