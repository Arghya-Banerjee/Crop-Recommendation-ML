
# Crop Recommendation using Machine Learning

![Img](https://user-images.githubusercontent.com/72212592/218297244-274dffed-9135-4674-8c75-ef450cfe86b1.png)


A crop recommendation model using a decision tree classifier is an AI-powered tool that provides personalized recommendations for farmers to optimize their crop production. This model uses a decision tree algorithm to analyze a wide range of factors that impact crop growth, such as soil elements like Nitrogen, Pottassium and Phosphorus, temperature, rainfall, soil ph.

By considering these various factors and the unique characteristics of each farm, the model is able to provide a customized recommendation for which crops will thrive in the specific conditions of each farm. This can help farmers maximize their yields and increase their profits while also ensuring the sustainability of their operations.

The decision tree classifier used in this model is a highly accurate and efficient machine learning technique that has been proven to be effective in many real-world applications. It is able to quickly analyze large amounts of data and make informed decisions based on the patterns it finds.

Overall, this crop recommendation model is a valuable resource for farmers looking to stay ahead of the curve and stay competitive in today's rapidly changing agricultural landscape. With its user-friendly interface and its ability to provide customized recommendations, it's never been easier to optimize crop production and achieve long-term success.

Source of Data: [Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)




## Installation

The Code is written in Python 3.9. If you don't have Python installed you can find it here. If you are using a lower
version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. Ta install the
required packages and libraries, run this command in the project directory after cloning the repository.

```bash
  pip install -r requirements.txt
```

## Run 

```bash
  python app.py
```

Once you run the script, the website should now be up and running on your local machine, and it can be viewed by visiting [localhost:5000](http://localhost:5000/) in your browser.
## Tech Stack

**Language:** [Python](https://www.python.org/)

**Libraries:** [Pandas](https://pandas.pydata.org/), [Numpy](https://numpy.org/), [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/), [skikit-learn](https://scikit-learn.org/stable/)

**Backend:** [Flask](https://flask.palletsprojects.com/en/2.2.x/)


## Features

- **Data Analysis:** The model analyzes a wide range of data, including Nitrogen, Pottassium and Phosphorus, temperature, rainfall, soil ph, to provide a comprehensive understanding of each farm's unique conditions.

- **Customized Recommendations:** Based on the data analysis, the model provides customized recommendations for which crops are best suited to each farm, helping farmers maximize their yields and profits.

- **Machine Learning Algorithms:** The model utilizes machine learning algorithms, such as decision tree classifiers, to analyze the data and provide recommendations.

- **User-Friendly Interface:** The model has a user-friendly interface that makes it easy for farmers to access and understand the recommendations, without requiring any technical knowledge.


## Code Structure

```
|   .gitattributes
|   app.py
|   Crop Recommendation ML.ipynb
|   crop_recommendationDTC.pkl
|   Img.png
|   LICENSE
|   output.txt
|   README.md
|   requirements.txt
|   
+---.ipynb_checkpoints
|       Crop Recommendation ML-checkpoint.ipynb
|       
+---app
+---Dataset
|       Crop_recommendation.csv
|       
+---static
|   \---css
|           style.css
|           
\---templates
        index.html        
```
## Deployment

This is project is deployed on Render.

Following are the specifics of Deployment:

- **Type** -> Web Service
- **Environment** -> Python
- **Region** -> Oregon
- **Build Command** -> ` pip install - r requirements.txt `
- **Deployment Command** -> ` gunicorn app:app `


