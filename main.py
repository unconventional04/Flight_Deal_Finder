from flight_class import Flight
import smtplib
import os
email_password=os.environ.get
MY_EMAIL="oyeludeferanmi@gmail.com"

url_for_iata="https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:_A"
home_city=input(f"Enter the IATA code for the nearest airport to you: If you don't know the IATA code, vist {url_for_iata}: \n ")
locations=input("Enter the IATA codes of the nearest airport to the cities you want to visits. Example response is DCA,BER,TAR.Use comma only to separate them \n")
lenght_of_stay=int(input("Enter the lenght of days for your desired stay in days: "))
locations_list=locations.split(",")
print(locations_list)
email_address=input("Enter your email address so we can send you emails daily for cheap flights: ")

for i in locations_list:
    flight=Flight(home_city, i)
    flight.flight_offers()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="oyeludeferanmi@gmail.com", password="rdpxuhizgczelgrr")
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=email_address,
                            msg=f"Subject: Best Flight Deal Offer for {home_city} to {i}! Notification\n\n We have gotten a cheap flight for you! A flight leaving on {flight.date} and  is for ${flight.price}. Go to {flight.url} to book quickly."
                            )

