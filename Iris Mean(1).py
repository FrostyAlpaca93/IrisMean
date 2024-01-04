#!/usr/bin/env python
# coding: utf-8

# # Introduction to Iris Dataset Analysis
# 
# Welcome to this Jupyter notebook, where we delve into the exploratory data analysis of the famous Iris dataset. This dataset, a staple in the field of data science and machine learning, offers a comprehensive look at the characteristics of three different species of the Iris flower - Iris Setosa, Iris Versicolor, and Iris Virginica.
# 
# In this analysis, our primary focus is to calculate and understand the mean values of the various features of these species - sepal length, sepal width, petal length, and petal width. This simple yet insightful exercise aims to provide a foundational understanding of how these species differ from each other in terms of these measurable characteristics.
# 
# This notebook is intended for beginners in data analysis and serves as a practical example of basic data manipulation and summarization techniques in Python. Let's dive into the world of the Iris flower and uncover the nuances of its species through data!

# Data Loading

# In[3]:


import pandas as pd

# Load CSV file
df = pd.read_csv('iris.csv')

# Display dataset
df.head()


# Data Exploration

# In[28]:


# Filter Data for each species



setosa_df = df[df['Species'] == 'Iris-setosa']
versicolor_df = df[df['Species'] == 'Iris-versicolor']
virginica_df = df[df['Species'] == 'Iris-virginica']


# In[29]:


# Mean Sepal Length

# Calculating the mean of the Sepal Length for each Iris species.
# This helps in understanding the average sepal length characteristic of each species.

mean_sepal_length_setosa = setosa_df['SepalLengthCm'].mean()
mean_sepal_length_versicolor = versicolor_df['SepalLengthCm'].mean()
mean_sepal_length_virginica = virginica_df['SepalLengthCm'].mean()

print(f"Setosa Sepal Length Mean is: {mean_sepal_length_setosa:.2f}")
print(f"Versicolor Sepal Length Mean is: {mean_sepal_length_versicolor:.2f}")
print(f"Virginica Sepal Length Mean is: {mean_sepal_length_virginica:2f}")


# In[43]:


# Mean Sepal Width

# Calculating the mean of the Sepal Width for each Iris species.
# This helps in understanding the average sepal width characteristic of each species.

mean_sepal_width_setosa = setosa_df['SepalWidthCm'].mean()
mean_sepal_width_versicolor = versicolor_df['SepalWidthCm'].mean()
mean_sepal_width_virginica = virginica_df['SepalWidthCm'].mean()

print(f"Setosa Sepal Width Mean is: {mean_sepal_width_setosa:.2f}")
print(f"Versicolor Sepal Width Mean is: {mean_sepal_width_versicolor:.2f}")
print(f"Virginica Sepal With Mean is: {mean_sepal_width_virginica:.2f}")


# In[52]:


# Mean Petal Length

# Calculating the mean of the Petal Length for each Iris species.
# This helps in understanding the average Petal Length characteristic of each species.

mean_petal_length_setosa = setosa_df['PetalLengthCm'].mean()
mean_petal_length_versicolor = versicolor_df['PetalLengthCm'].mean()
mean_petal_length_virginica = virginica_df['PetalLengthCm'].mean()

print(f"Setosa Petal Length Mean is: {mean_petal_length_setosa:.2f}")
print(f"Versicolor Petal Length Mean is: {mean_petal_length_versicolor:.2f}")
print(f"Virginica Petal Length Mean is: {mean_petal_length_virginica:.2f}")


# In[55]:


# Mean Petal Width

# Calculating the mean of the Petal Width for each Iris species.
# This helps in understanding the average Petal Width characteristic of each species.

mean_petal_width_setosa = setosa_df['PetalWidthCm'].mean()
mean_petal_width_versicolor = versicolor_df['PetalWidthCm'].mean()
mean_petal_width_virginica = virginica_df['PetalWidthCm'].mean()

print(f"Setosa Petal Width mean is: {mean_petal_width_setosa:.2f}")
print(f"Versicolor Petal Width mean is: {mean_petal_width_versicolor:.2f}")
print(f"Virginica Petal Witdth mean is: {mean_petal_width_virginica:.2f}")


# # Summary
# 
# Highest Sepal Length Mean: Virginica at 6.6cm
# Lowest Sepal Length Mean: Setosa at 5.01cm
# 
# Highest Sepal Width Mean: Setosa at 3.42cm
# Lowest Sepal Width Mean: Versicolor at 2.77cm
# 
# Highest Petal Length Mean: Virginica at 5.55cm
# Lowest Petal Length Mean: Setosa 1.46cm
# 
# Highest Petal Width Mean: Virginica 2.03cm
# Lowest Petal Width Mean: Setosa 0.24cm

# # Conclusion
# 
# Through this notebook, we have successfully computed and analyzed the mean values of various features of the Iris species. Our findings reveal distinct patterns and differences among Iris Setosa, Iris Versicolor, and Iris Virginica, particularly in terms of sepal length, sepal width, petal length, and petal width.
