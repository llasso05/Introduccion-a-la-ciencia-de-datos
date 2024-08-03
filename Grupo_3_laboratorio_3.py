import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading data
df = pd.read_csv(r"C:\Users\chima\repos\Maestria\Intro_a_la_ciencia_de_datos\Introduccion-a-la-ciencia-de-datos\BGG_Games.csv")

# Title
st.title("Board Games Overview")

# Metrics
st.subheader("Overview")
total_games = len(df)
avg_rating = df['Rating Average'].mean()
avg_complexity = df['Complexity Average'].mean()

st.metric("Total Games", total_games)
st.metric("Average Rating", f"{avg_rating:.2f}")
st.metric("Average Complexity", f"{avg_complexity:.2f}")

# Top 10 Games by User Ratings
st.subheader('Top 10 Games by Number of User Ratings')
top_rated = df.nlargest(10, 'Users Rated')
fig, ax = plt.subplots()
sns.barplot(x='Users Rated', y='Name', data=top_rated, ax=ax)
st.pyplot(fig)

# Distribution of Games by Min Players
st.subheader('Games by Minimum Recommended Players')
min_players_dist = df['Min Players'].value_counts()
st.bar_chart(min_players_dist)


