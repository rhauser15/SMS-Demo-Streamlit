import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from vardata import *
from Config import *

##demo send messages
from twilio.rest import Client

# Your Account SID from twilio.com/console

# Your Auth Token from twilio.com/console



client = Client(account_sid, auth_token)

leEngineer = "Roger"
satUp = 516
satDown = 0




####User design###
st.title('Starlink Monitoring')

st.write('Current Geolocation of Base stations and satellites')





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
    message = client.messages.create(
        to="+19199498424",
        from_="+12052735082",
        body="alert")



    print(message.sid)
    print(leEngineer + " has been noified")

    st.write('1 Satellite(s) are down. Roger has been notified')




#sidebar oganization
option = st.sidebar.selectbox(
    'Lead Engineer on-Call',
     le2['Lead Engineers'])

leEngineer = option
