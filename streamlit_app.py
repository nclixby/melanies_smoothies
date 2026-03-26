# Import python packages.
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app.
st.title(":apple: Customize Your Smoothie :mango:")
st.write(
  """Replace this example with your own code!
  **And if you're new to Streamlit,** check
  out our easy-to-follow guides at
  [docs.streamlit.io](https://docs.streamlit.io).
  """
)

name_on_order = st.text_input('Name on Smoothie')
st.write('The name on your Smoothie will be ', name_on_order)

cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.orders").filter(col("ORDER_FILLED") == 0).to_pandas()
editable_df = st.data_editor(my_dataframe)
