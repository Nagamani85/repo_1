import streamlit
streamlit.title(' my parents new healthy dinner')
streamlit.header('🥣Breakfast Menu')
streamlit.text('🥗 Omege3 and Blueberry Oatmeal')   
streamlit.text('🐔 Kale Spinach and Rocket Smoothy')
streamlit.text('🥑🍞Hard-Boiled Free Range Egg ')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

      
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

#Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.Fruit))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)


streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado' , 'Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]



