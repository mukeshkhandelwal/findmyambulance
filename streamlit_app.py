import streamlit as st

from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
#https://github.com/aghasemi/streamlit_js_eval/blob/master/example.py
# Returns user's location after asking for permission when the user clicks the generated link with the given text

# location = geo.streamlit_geolocation()
#print (location)
st.title("Book My Ambulance")
areas_served = ['560035', '560103', '560001', '561111']
pincode = st.text_input('Whats your PIN CODE')


if st.button('Check availability'):
    have_it = pincode.lower() in areas_served
    #get the user's location
    loc = get_geolocation()

    st.write(f"Your coordinates are {loc}")

    if have_it:
        st.text('We have an ambulance..sending it soon!')
    else:
        st.text('Sorry, we don\'t serve your area yet.')

# Share something using the sharing API
create_share_link(dict({'title': 'streamlit-js-eval', 'url': 'https://github.com/aghasemi/streamlit_js_eval', 'text': "A description"}), "Share a URL (only on mobile devices)", 'Successfully shared', component_key = 'shdemo')

