import streamlit as st 
import requests 
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title='My Webpage', page_icon=":tada:",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")       



lottie_coding = "https://lottie.host/c9cde6b5-f0bd-4749-965d-dd3e13b41faf/Wp4tXTzagB.json"
img_monthly_tracker = Image.open('/Users/guzalmaksud/Downloads/my_webpage/images/Screenshot 2024-12-22 at 13.58.39.png')
img_questionnaire = Image.open('/Users/guzalmaksud/Downloads/my_webpage/images/Screenshot 2024-12-22 at 13.47.02.png')
with st.container():
    st.subheader("Hi, I am Umida :wave: ")
    st.title('A Data Scientist From Norway')
    st.write('I am passionate about creating things I thought I would never be able to!')

with st.container():
    st.write("---")

    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What is this blog about?")
        st.write('##')
        st.write(
            """
            In this blog I want to store all the things I have created so far and will create in the future, such as
            - webpages or, in another word, projects
            - games using Python
            - my writings
            - etc
            """
)
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))

    with image_column:
        st.image(img_monthly_tracker)
    with text_column:
        st.subheader("Monthly Tracker Website Using Flask")
        st.write("""
                 This is a website to track and store your monthly spendings and incomes. It is easy to follow each person's finances in a household, with diagrams that clearly shows who spent more so that you have a proof to use against in an argument ;)
                """)
        st.markdown("[See my Github page to get all the codes ...](https://github.com/itsumida/Monthly-finances-tracker-app)")
with st.container():
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img_questionnaire)
    with text_column:
        st.subheader("A Questionnaire for school")
        st.write("""
                This is a survey for certain class at school. The results are in a separate page under the name of summary.
                """)
        st.markdown("[See my Github page to get all the codes ...](https://github.com/itsumida/Database-2024/blob/main/final_form2024.zip)")

with st.container():
    st.subheader("Other : ")
    st.markdown("[A personal website for an influencer: ](https://bekolimjon.com/)")
    st.markdown("[A group project on analysing and predicting 3 different datasets: ](https://github.com/itsumida/machine-learning-2024)")

with st.container():
    st.write("---")
    st.header("Get in touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/umidajade@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder = "Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
