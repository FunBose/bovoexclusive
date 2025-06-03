# RUN WITH C:\Users\IniOluwa\BOVO\venv\Scripts\python.exe C:\Users\IniOluwa\BOVO\venv\Scripts\streamlit.exe run C:\Users\IniOluwa\BOVO\bovoexclusivefashion.py
# https://pypi.org/project/streamlit-carousel/
# Set-ExecutionPolicy Unrestricted -Scope Process

import streamlit as st # pip install streamlit
from streamlit_carousel import carousel # pip install streamlit-carousel 
from PIL import Image # pip install pillow
import pandas as pd
def wide_space_default():
    st.set_page_config(layout= "wide")  #(layout=“wide”)

wide_space_default()

st.info('# BOVO Exclusive International Fashion Designer')
st.header('Bespoke Fashion Designing at affordable prices')
st.subheader('Based in South Korea, but takes order and deliver anywhere, any time')

st.info("## The CEO of BOVO: Victoria Ogunbo (+82-10-6443-0782; bovoexclusive@gmail.com)")
#img = Image.open("Bovo_Icon.JPG")
# #img = Image.open(r"C:\Users\Ogunbo\Documents\Language_subtitles\Jide_Ogunbo_Photo.jpg")
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(image=Image.open("Bovo_Icon.JPG")) #,width=300)
with left_co:
    st.image(image=Image.open("Bovo_Icon_Sitting.jpg")) #,width=300) 
#==================================================================

st.header('African Day Attire')
st.info("## Beautiful Nigerian style")
st.image(image=Image.open("Mrs_Inex_4.png")) 

st.success("## Slides: Beautiful Nigerian style")
test_inex1 = [
    dict(
        title="Slide 1",
        text="Elegant",
        img="Mrs_Inex_1.png",
        
    ),
    dict(
        title="Slide 2",
        text="Pretty",
        img="Mrs_Inex_2.png",
        
    ),
    dict(
        title="Slide 3",
        text="Pretty",
        img="Mrs_Inex_3.png",
        
    ),
    dict(
        title="Slide 4",
        text="Pretty",
        img="Mrs_Inex_4.png",
        
    ),
    dict(
        title="Slide 5",
        text="Pretty",
        img="Mrs_Inex_5.png",
        
    ),
    
]
carousel(items=test_inex1)

st.header('Men Senator Suit')
st.info("## Gorgeous")
colj1, colj2 = st.columns(2)
with colj1:
    st.image(image=Image.open("Jide_Suit_Like_1.png")) #,width=300)
with colj2:
    st.image(image=Image.open("Jide_Suit_Like_2.png")) #,width=300) 

# st.image(image=img,width=100)
st.header('Women Evening Dresses')
st.info("## Elegant Evening Dresses")
st.image(image=Image.open("Evening_dress_1.png")) 

st.success("## Diverse culture")
st.image(image=Image.open("Evening_dress_2.png")) 

st.info("## Pretty Evening Dresses")
st.image(image=Image.open("Evening_dress_3.png")) 

st.info("## Pretty Evening Dresses")
st.image(image=Image.open("Evening_dress_4.png")) 
st.info("## Exotic Evening Dresses")
st.image(image=Image.open("Evening_dress_5.png")) 
st.info("## Beautiful Evening Dresses")
st.image(image=Image.open("Evening_dress_6.png")) 
st.info("## Pretty Evening Dresses")
st.image(image=Image.open("Evening_dress_7.png")) 
st.info("## Elegant Evening Dresses")
st.image(image=Image.open("Evening_dress_8.png")) 

st.info("## Safari Suit")
col1s, col2s = st.columns(2)
with col1s:
    st.image(image=Image.open("Safari_man_1.png")) #,width=300)
with col2s:
    st.image(image=Image.open("Safari_man_2.png")) 


st.success("## A-flare Gowns")
col1g, col2g, col3g, col4g = st.columns(4)
with col1g:
    st.image(image=Image.open("Elderly_woman_1.png")) #,width=300)
with col2g:
    st.image(image=Image.open("Elderly_woman_2.png")) 
with col3g:
    st.image(image=Image.open("Elderly_woman_3.png")) #,width=300)
with col4g:
    st.image(image=Image.open("Elderly_woman_4.png")) 

st.warning("## Kaftan")
col1, col2,col3,col4,col5 = st.columns(5)
with col1:
    st.image(image=Image.open("Grandma_Twins_1.png")) #,width=300)
with col2:
    st.image(image=Image.open("Grandma_Twins_2.png")) 
with col3:
    st.image(image=Image.open("Grandma_Twins_3.png"))
with col4:
    st.image(image=Image.open("Grandma_Twins_4.png")) 
with col5:
    st.image(image=Image.open("Grandma_Twins_5.png")) 

st.info("## Velvet Ruffle Front and Back Gown 1")
col1v, col2v,col3v,col4v,col5v,col6v = st.columns(6)
with col1v:
    st.image(image=Image.open("Sis_Favor_1.jpg")) #,width=300)
with col2v:
    st.image(image=Image.open("Sis_Favor_2.jpg")) 
with col3v:
    st.image(image=Image.open("Sis_Favor_3.jpg"))
with col4v:
    st.image(image=Image.open("Sis_Favor_4.jpg")) 
with col5v:
    st.image(image=Image.open("Sis_Favor_5.jpg"))     
with col6v:
    st.image(image=Image.open("Sis_Favor_5.jpg"))   


st.success("## Slides: Velvet Ruffle Front and Back Gown 1")
test_items = [
    dict(
        title="Slide 1",
        text="Elegant",
        img="Sis_Favor_1.jpg",
        
    ),
    dict(
        title="Slide 2",
        text="Pretty",
        img="Sis_Favor_2.jpg",
        
    ),
    dict(
        title="Slide 3",
        text="Lettuce white light container",
        img="Sis_Favor_3.jpg",
        
    ),
    dict(
        title="Slide 4",
        text="Graceful",
        img="Sis_Favor_4.jpg",
        
    ),
    dict(
        title="Slide 5",
        text="Exquisite",
        img="Sis_Favor_5.jpg",
        
    ),
    dict(
        title="Slide 6",
        text="Appealing",
        img="Sis_Favor_6.jpg",
        
    ),
]
carousel(items=test_items)

st.warning("## Velvet Ruffle Front and Back Gown 2")
col1v2, col2v2,col3v2,col4v2,col5v2,col6v2 = st.columns(6)
with col1v2:
    st.image(image=Image.open("Favor_backView_1.jpg")) #,width=300)
with col2v2:
    st.image(image=Image.open("Favor_backView_2.jpg")) 
with col3v2:
    st.image(image=Image.open("Favor_backView_3.jpg"))
with col4v2:
    st.image(image=Image.open("Favor_backView_4.jpg")) 
with col5v2:
    st.image(image=Image.open("Favor_backView_5.jpg"))     
with col6v2:
    st.image(image=Image.open("Favor_backView_5.jpg"))   

st.info("## Slides: Velvet Ruffle Front and Back Gown 2")

test_items2 = [
    dict(
        title="Slide 1",
        text="Elegant",
        img="Favor_backView_1.jpg",
        
    ),
    dict(
        title="Slide 2",
        text="Pretty",
        img="Favor_backView_2.jpg",
        
    ),
    dict(
        title="Slide 3",
        text="Lettuce white light container",
        img="Favor_backView_3.jpg",
        
    ),
    dict(
        title="Slide 4",
        text="Graceful",
        img="Favor_backView_4.jpg",
        
    ),
    dict(
        title="Slide 5",
        text="Exquisite",
        img="Favor_backView_5.jpg",
        
    ),
    dict(
        title="Slide 6",
        text="Appealing",
        img="Favor_backView_6.jpg",
        
    ),
]
carousel(items=test_items2)

st.info("## Safari Jacket")
col1ss, col2ss,col3ss, col4ss = st.columns(4)
with col1ss:
    st.image(image=Image.open("Deacon_Ibeneme_1.png")) #,width=300)
with col2ss:
    st.image(image=Image.open("Deacon_Ibeneme_2.png")) 
with col3ss:
    st.image(image=Image.open("Deacon_Ibeneme_3.png")) #,width=300)
with col4ss:
    st.image(image=Image.open("Deacon_Ibeneme_4.png")) 

st.success("## Slides: Safari Jacket")
ibeneme = [
    dict(
        title="Slide 1",
        text="Elegant",
        img="Deacon_Ibeneme_1.png",
        
    ),
    dict(
        title="Slide 2",
        text="Pretty",
        img="Deacon_Ibeneme_2.png",
        
    ),
    dict(
        title="Slide 3",
        text="Lettuce white light container",
        img="Deacon_Ibeneme_3.png",
        
    ),
    dict(
        title="Slide 4",
        text="Graceful",
        img="Deacon_Ibeneme_4.png",
        
    ),
    
]
carousel(items=ibeneme)

#=====================================================================
st.header('Women in Magenta African Print')
st.info("## Beautiful Magenta African Prints")
st.image(image=Image.open("Sis_Vicky_1.png")) 

st.success("## Slides: Beautiful Magenta African Prints")
test_vicky1 = [
    dict(
        title="Slide 1",
        text="Elegant",
        img="Sis_Vicky_1.png",
        
    ),
    dict(
        title="Slide 2",
        text="Pretty",
        img="Sis_Vicky_2.png",
        
    ),
    dict(
        title="Slide 3",
        text="Pretty",
        img="Sis_Vicky_3.png",
        
    ),
    
]
carousel(items=test_vicky1)


#df = pd.read_csv("Grade_5_Science_Experiment_Log.csv")
##st.dataframe(df.head())
#st.dataframe(df, height=None) # To display all rows with scrollbar if needed
