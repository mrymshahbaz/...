import requests
import json

def get_weather_data(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    url = f"{base_url}appid={api_key}&q={city_name}&units=metric"  

    try:
        response = requests.get(url)
        response.raise_for_status()  
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"خطا در دریافت اطلاعات: {e}")
        return None


def print_weather_info(weather_data):
    if weather_data:
        try:
            main_data = weather_data['main']
            weather_desc = weather_data['weather'][0]['description']
            city = weather_data['name']

            temp = main_data['temp']
            humidity = main_data['humidity']
            pressure = main_data['pressure']

            print(f"وضعیت آب و هوا برای شهر {city}:")
            print(f"  وضعیت: {weather_desc}")
            print(f"  دما: {temp} درجه سانتیگراد")
            print(f"  رطوبت: {humidity}%")
            print(f"  فشار هوا: {pressure} hPa")

        except KeyError as e:
            print(f"خطا در پردازش داده ها: کلید {e} یافت نشد")
    else:
        print("داده های آب و هوا برای شهر مورد نظر دریافت نشد.")


if __name__ == "__main__":
    api_key = "36505626f1e53a6de24fd1d1b59d081b"  
    city_name = input("نام شهر مورد نظر را وارد کنید: ")
    weather_data = get_weather_data(city_name, api_key)
    print_weather_info(weather_data)