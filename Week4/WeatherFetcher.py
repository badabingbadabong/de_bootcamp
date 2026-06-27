import requests

url = "https://wttr.in/?format=j1"


response = requests.get(url)

if response.status_code == 200:
    data = response.json() 
    # print(data)

    # try:
    #     with open("weather.csv", "x", encoding="utf-8"):
    #         pass
    # except FileExistsError:
    #     print("File already exists")


    
    # with open("weather.csv","a", encoding="utf-8") as file:
    #     file.write(str(data) + "\n")
    




    current = data["current_condition"][0]

    with open("weather.csv","a", encoding="utf-8") as file:
         
         if file.tell() == 0:
            file.write("temp_C,humidity,FeelsLikeC\n")


         file.write(
            current["temp_C"] + "," +
            current["humidity"] + "," +
            current["FeelsLikeC"] + "," +"\n"
            )


    print("Data Saved")

else:
    print("Error")
