from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from twilio.twiml.messaging_response import MessagingResponse

url = "https://coronaclusters.in/west-bengal"
def get_status():
    response = requests.get("https://coronaclusters.in/west-bengal")
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')
    soup.prettify

    result = []

    data = soup.find("div", {'id':"data"})
    card_stats = data.find("div", {'class': 'col-12 card-stats'})
    for div in card_stats.findChildren("div", recursive=False):
        childs = div.findChildren("div")
        for child in childs:
            result.append(child.getText())

    confirmed = result[1]
    confirmed_no = result[2].split('[')[0]
    active = result[5]
    active_no = result[6].split('[')[0]
    recovered = result[9]
    recovered_no = result[10].split('[')[0]
    deaths = result[13]
    deaths_no = result[14].split('[')[0]

    return confirmed, confirmed_no, active, active_no, recovered, recovered_no, deaths, deaths_no

app = Flask(__name__)

@app.route('/') 
def test():
    #resp = MessagingResponse()
    #resp.message("Working!")
    #return str(resp)
    return f"Working"

@app.route('/track', methods= ['POST', 'GET']) 
def sendCOVIDStatus(): 
    confirmed, confirmed_no, active, active_no, recovered, recovered_no, deaths, deaths_no = get_status()
    resp = MessagingResponse()
    resp.message(f"COVID-19 STATS\nURL: {url}\nState: West Bengal\n{confirmed}: {confirmed_no}\n{active}: {active_no}\n{recovered}: {recovered_no}\n{deaths}: {deaths_no}")
    #resp.message(f"You said: Haha nothing:)")
    return str(resp)
    #return "Covid"

# main driver function 
if __name__ == '__main__': 

    app.run(debug= True)
