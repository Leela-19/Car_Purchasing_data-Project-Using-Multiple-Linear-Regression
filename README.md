
# CAR_PURCHASING_DATA Project Using Multiple Linear Regression

In This Repo I am completely posting the Data Preprocessing on structure Data. Since Data Preprocessing was one of the most challenging task for many of the ML Engineers I came-up with this repo to share all the important techniques which are usefull to clean the data.

# Steps to follow for developing ML Models

    - Data collecting 
    - Selecting Required Packages 
    - Handling NUll values for Numerical and Categorical data 
    - converting Categorical_data features to Numerical features
    - Selecting the Best Features for the Model
    - This techniques come under Feature Selection                          
    - Developing few Model
    - Selecting Best model to get better performances on test data  
    - Saving the Model 

# Skills
    - Pyhton
    - numpy
    - pandas
    - scikit learn

 
# Acknowledgements

 -sklearn library
 https://scikit-learn.org/stable/

 # Feature selection for structure data

## Regression
Regression is  a  statistical  approach  used  to  analyse  the  relationship between a dependent variable (target variable) and one or more independent variables (predictor variables). The objective is to determine the most suitable function  that  characterizes  the  connection  between  these  variables. It  is  a supervised  machine  learning  technique,  used  to  predict  the  value  of  the dependent variable for new, unseen data. It models the relationship between the input features and the target variable, allowing for the estimation or prediction of numerical values.

![image](https://github.com/user-attachments/assets/ae7f5bdc-8b44-4069-871b-6e561d0595e3)

Mainly there are 4 types of regression
There are :
1.  Simple Linear Regression
2.  Multiple Linear Regression
3.  Regularization
4.  Polynomial Linear Regression
Firstly, linear regression is nothing but a straight line.
             i.e.  y=mx + c
To the operation on linear regression. We have to import linear regression class from the model selection function from the sklearn library.
## Simple Linear Regression:
We have only one independent and one dependent feature for the simple linear regression.
## Multiple Linear Regression:
We  have  only  one  dependent  and  multiple  independent  features  for multiple linear regression.Regularization:
It is used to reduce the overfitting problem. It can be implemented in two different mathematics i.e. regularization is divided into two types .
They are:
1.  Ridge Regression
2.  Lasso Regression
## Ridge Regression:
It is also known as L2 Regression. It tries to increase the accuracy of the data and decreases the loss in the data.
## Lasso Regression: 
It is also known as L1 Regression. It tries to increase the accuracy of the data and decreases the loss in the data and also in any case the slope values becomes zero then it will remove that particular column from the data.
## Polynomial Regression:
A  form  of  regression  analysis  in  which  the  relationship  between  the independent variable x and the dependent variable y is modeled as an nth degree polynomial in x.

# Complete Operation of the dataset:

### Step 1:

Firstly, we read the dataset by giving it path and also by using pandas we can view the dataset in it’s original form.

### Step 2:

Then we should check the dependent and independent features by checking this we can come to know weather it is simple linear regression or multiple linear regression.
###Step 3:
Now, check weather there is unwanted features in the dataset. If it is there then remove the feature. 

### Step 4:

Divide the independent and dependent features into two different variables i.e. X , y and then give these two variables to the train test split module and in it add test size and random state. Here, test size is nothing but giving value that how much the test data should be divided and random state will protect the data which is already executed without changing them every step of running.

### Step 5:

Then import the linear regression class and give the splitted features by the train test split by this the dataset will be given to the algorithm and then the algorithm will be trained.

### Step 6:

And then predict the values by giving the independent features. And then find the accuracy for the original values and predicted values by importing r2_score function from the metrics method  from the sklearn library.

### Step 7:

Also find the loss by giving the original values and predicted values to the loss functions. There are the loss functions they are mean squared error, absolute square error, R squared error.by importing the loss function from metrics from the sklearn.

### Step 8:

Repeat the above 5,6,7 steps by giving test data instead of train data so, that you will get  test data accuracy and loss.

### Step 9:

From the above steps we will get the exact results of the given dataset so, that we can decide weather the dataset is good or bad.

# Conclusion

In this project, we applied a multiple linear regression model to predict car purchase amount based on various factors such as age, gender, annual salary, credit card debt, net worth. The goal was to understand how these variables influence car purchase amount and to develop a model that can estimate the purchase amount of a car given its characteristics.
 

# 🔗 Links

https://www.linkedin.com/in/leela-usha-sri-0418b0267/


# Support

For support, email leelaushasri19@gmail.com 


