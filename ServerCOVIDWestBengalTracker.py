from COVIDWestBengalTracker import url, state, stateIndex, stateValues
from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse
  

app = Flask(__name__) 

@app.route('/') 
def test():
    resp = MessagingResponse()
    resp.message("Working!")
    return str(resp)

@app.route('/track', methods= ['POST']) 
def sendCOVIDStatus(): 
    stateName = state
    index = stateIndex
    values = stateValues
    resp = MessagingResponse()
    resp.message(f"COVID-19 STATS\nURL: {url}\nState: {stateName}\n{index[0]}: {values[0]}\n{index[1]}: {values[1]}\n{index[2]}: {values[2]}\n{index[3]}: {values[3]}")
    return str(resp)

# main driver function 
if __name__ == '__main__': 

    app.run(debug= True)
