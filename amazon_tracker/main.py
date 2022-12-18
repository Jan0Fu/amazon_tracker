from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

email = ""
password = ""


url = "https://www.amazon.com/Oculus-Quest-Advanced-All-One-Virtual/dp/B099VMT8VZ/ref=sr_1_3?keywords=oculus+quest+2&qid=1671349190&sprefix=ocul%2Caps%2C341&sr=8-3"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15",
    "Accept-Language": "en-GB,en;q=0.9"
}
response = requests.get(url, headers=headers)
website_html = response.text

soup = BeautifulSoup(website_html, "lxml")
price_tag = soup.find(name="span", id="priceblock_ourprice").getText()
price = float(price_tag.split("$")[1])
print(price)

smtp = smtplib.SMTP("smtp.gmail.com")
