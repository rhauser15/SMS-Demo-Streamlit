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
auth_token  = "b6a81c60b866a329e2612b69d84824d1"

client = Client(account_sid, auth_token)





####User design###
st.title('Starlink Monitoring')

st.write('Current Geolocation of Base stations and satellites')




#Plotting map data
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

df = pd.DataFrame({
  'Total Satellites Deployed': [516],
  'Satellites Up': [516],
  'Satellites Down': [0]
})

df

le = pd.DataFrame({
    'Lead Engineers': ["Roger", "Ted", "Tyrell"],
    'Conact Numbers': [+19199498424, +19199498424, +19199498424]
})

le

#Interactive checkbox
if st.button('Text'):
    message = client.messages.create(
        to="+19199498424",
        from_="+14158424144",
        body="")

    print(message.sid)
    print("numberTexted")



#sidebar oganization
option = st.sidebar.selectbox(
    'Lead Engineer on-Call',
     le['Lead Engineers'])

'Engineer:', option
