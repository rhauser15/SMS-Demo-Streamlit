import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

##demo send messages
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC2bf09b1e538b1d9094430a7193e5e51f"
# Your Auth Token from twilio.com/console
auth_token  = "34801aa80b890b0579c1c1064351d580"

client = Client(account_sid, auth_token)

leEngineer = "Roger"
satUp = 0
satDown = 516



####User design###
st.title('Starlink Monitoring')

st.write('Current Geolocation of Base stations and satellites')




#Plotting map data
map_data = pd.DataFrame(
    np.random.randn(516, 2) / [10, .1] + [34.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

#Chart
df = pd.DataFrame({
  'Total Satellites Deployed': [516],
  'Satellites Up': [satUp],
  'Satellites Down': [satDown]
})

df

le = pd.DataFrame({
    'Lead Engineers': ["Roger", "Ted", "Tyrell"],
    'Contact Numbers': [+19199498424, +19199498424, +19199498424]
})

le.set_index('Lead Engineers', inplace=True)

le

le2 = pd.DataFrame({
    'Lead Engineers': ["Roger", "Ted", "Tyrell"],
    'Contact Numbers': [+19199498424, +19199498424, +19199498424]
})

#Interactive checkbox
if st.button('Sattelite Down Test'):
    #message = client.messag'Lead Engineers's.create(
       #to="+19199498424",
      # from_="+14158424144",
      # body="alert")

    #print(message.sid)
    print(leEngineer + " Texted")
    st.write(leEngineer + "Texted")



#sidebar oganization
option = st.sidebar.selectbox(
    'Lead Engineer on-Call',
     le2['Lead Engineers'])

leEngineer = option
'Engineer:', option
