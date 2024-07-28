# **Cardiovascular Risk Assessment**

Heart Diseases being one of the leading causes of mortality worldwide is a significant concern that needs to be addressed immediately. This project aims to analyse user's biometric data and determine their susceptibility to heart disease.


### **Data Description**
The dataset used in this project contains the following columns:

    1. Age: The age of the patient in integer form.
    
    2. Sex: The gender of the patient either male or female(1 or 0).

    3. Chest Pain type(cp): Important feature that indicates the type of pain that  occurs in the chest and possible factors for the same (Ranging from value 1 to value 4).

    4. Resting Blood Pressure(trestbps): The measure of blood pressure of the patient when the patient is in the state of rest.

    5.Serum Cholesterol(chol): The levels of High Density Lipoproteins and Low Density Lipoproteins present in the blood stream or body.

    6.Fasting Blood Sugar(fbs): The measure of level sugar present in the blood after a fasting of over 8-9 hours.

    7.Resting ECG(restecg): The measure of Heart Rate of the patient when the patient is at rest.

    8.Maximum Heart Rate achieved(thalach): The maximum level of Heart Rate achieved when the patient undergoes stress test or exercise tolerance test.
    
    9.Exercise Induced Angina(exang): Parameter that indicates whether the patient suffers from a chest pain during exercise or not. 
    
    10. ST depression induced by Exercise Relative to Rest(oldpeak): It is difference of deviation in ST segment when in the state of Exercise relative to Rest.
    
    11. Slope of Peak exercise ST segment(slope):  Feature that helps assess the heart's response to exercise and can indicate underlying cardiac conditions.
    
    12. Number of Major vessels colored(ca): Colored fluoroscopy of the major vessels that indicate the extent to which the arteries are blocked.
    
    13. Thalassemia(thal): Refers to the type of blood disorder inherited by the patient.
    
    14. Target: Indicates whether the patient is a susceptible to heart disease or not.
    



### **Steps Involved:**

    1. **Data Preprocessing**:
        - Download and Load the dataset from UC Irvene data repository for Heart Disease.
        - Encode categorical variables using one-hot encoding.
        - Split the data into training and testing sets.

    2. **Model Training & Testing**:
        - Test & Train seven different Machine Learning Models including:
            --> Logistic Regression
            --> K-Nearest Neighbors
            --> Support Vector Machines
            --> Naive Bayes Classifier
            --> Decision Trees
            --> Random Forest
            --> Extreme Gradient Boosting
        - Test & Train one Deep Learning including:
            --> Neural Networks

    3. **Model Evaluation**:
        - Predict whether the patient is a Heart Disease patient or not.
        - Evaluate the models using metrics such as Precision, Recall, F1 score and overall Accuracy of the model.

    4. **Visualization**:
        - Plot graphs that indicate the importance of various features in determing the final prediction.
        - Plot graphs indicating variety of observations observed between features such as Age, Sex, Type of Angina and many more in the form of graphs such as Violin plots, Box plots and Bar plots.
        - Plot graphs displaying the comparisons for different values of accuracy between each Machine Learning models and the Deep Learning model.

### **Results**:
    - The model that predicts the presence of Heart Disease with most accuracy is the Random Forest model.
    - The Random Forest model produced an accuracy of 80%.

***The Heart Disease prediction models developed in this project provide a solid foundation for predicting the presence or absence 0f Heart Disease. While the Random Forest model captures the basic relationships, analyses the different variables and makes predictions accordingly, the web interface acts as a medium of communication between the User and the trained Machine Learnig model. 
Future work can focus on incorporating additional features, exploring more advanced automation techniques, and fine-tuning the models for even better accuracy.***
