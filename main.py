import  langchain_helper as lch
import streamlit as st

st.title("Pet Name Generator")

User_animal_type = st.sidebar.selectbox("what is your pet name?",("Dog","Cat","Rat","Fish","Birds","Rabbit"))

if User_animal_type == "Dog":
    pet_color = st.sidebar.text_input(label="what color is your pet?",max_chars=12)


if User_animal_type =="Cat":
    pet_color =st.sidebar.text_input(label="what color is your pet?",max_chars=12)

if User_animal_type =="Rat":
    pet_color =st.sidebar.text_input(label="what color is your pet?",max_chars=12)

if User_animal_type =="Fish":
    pet_color =st.sidebar.text_input(label="what color is your pet?",max_chars=12)

if User_animal_type =="Birds":
   pet_color =  st.sidebar.text_input(label="what color is your pet?",max_chars=12)

if User_animal_type =="Rabbit":
    pet_color = st.sidebar.text_input(label="what color is your pet?",max_chars=12)


if pet_color:
    # st.button("Refresh")'
    # if  st.button("Refresh"):
        responce = lch.generate_pet_name(User_animal_type,pet_color) 
        st.text(responce['pet_name'])
# if pet_color :
#     # st.button("Refresh")
#     responcel =  lch.generate_pet_name(User_animal_type,pet_color)
        # st.button("Refresh"),st.text( responce['pet_name'])





























