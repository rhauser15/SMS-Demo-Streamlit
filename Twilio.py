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

message = client.messages.create(
    to="+19199498424",
    body="Hello from Python!")

print(message.sid)



####User design###
st.title('My Motherfucking stupid Twilio Demo')

st.write('Test2')

#making a table
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

#magic commands??

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

#Draw a line chart
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#Plotting map data
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


#Interactive checkbox
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)


#slect checkbox
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option


#sidebar oganization
option = st.sidebar.selectbox(
    'Which number do you like best of ths?',
     df['first column'])

'You selected:', option
