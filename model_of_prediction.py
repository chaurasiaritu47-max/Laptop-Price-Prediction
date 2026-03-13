import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report , confusion_matrix
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge
from sklearn.model_selection import learning_curve
import joblib



df = pd.read_csv(r'D:/Laptop_interface/final_laptop_datascrape.csv', encoding='ISO-8859-1')   
df.head()
df.shape
df.info()
#df.drop(columns=['Product_name','Description'], inplace=True)
df.info()
sns.heatmap(df.isnull())
df.isnull().sum()
#Ram correction
df['RAM_Size'] = df['RAM_Size'].str.extract('(\d+)')
df['RAM_Size'] = df['RAM_Size'].replace('Not Available', 0)
#df['RAM_Size'] = df['RAM_Size'].str.replace('GB DDR5 RAM',' ')
#df['RAM_Size'] = df['RAM_Size'].str.replace('GB DDR4 RAM',' ')
df['RAM_Size'] = df['RAM_Size'].fillna(0)  # Fill NaN values with 0
df['RAM_Size'] = df['RAM_Size'].astype('int32')
print(df['RAM_Size'])

#Processor_Generation
df['Processor_Generation'] = df['Processor_Generation'].str.extract('(\d+)')
df['Processor_Generation'] = df['Processor_Generation'].replace('Not Available', 0)
df['Processor_Generation'] = df['Processor_Generation'].fillna(0)
df['Processor_Generation'].fillna(0)
df['Processor_Generation'] = df['Processor_Generation'].astype('int32')

#review
print(df['Reviews'])
df['Reviews'] = df['Reviews'].replace('Not Available', 0)
df['Reviews'] = df['Reviews'].fillna(0)
df['Reviews']=df['Reviews'].astype('float64')
print(df['Reviews'])

#converting storage capacity from TB to GB
print(df['Storage_Capacity'])
print("Unique values before conversion:", df['Storage_Capacity'].unique())

# Function to convert storage capacity to GB
def convert_to_gb(Storage_Capacity):
  if pd.isna(Storage_Capacity):
    return np.nan
  Storage_Capacity = str(Storage_Capacity).strip().upper()  # Normalize case and strip spaces

    # Remove any unexpected characters or additional spaces
  Storage_Capacity = Storage_Capacity.replace(' ', '').replace('GB', ' GB').replace('TB', ' TB')

    # Handle "Not Available"
  if Storage_Capacity == 'Not Available' or Storage_Capacity == '0':
    return np.nan  # Optionally replace '0' with NaN to handle it later

    # Convert TB to GB
  if 'TB' in Storage_Capacity:
    return float(Storage_Capacity.replace('TB', '').strip()) * 1024  # Convert TB to GB
  elif 'GB' in Storage_Capacity:
    return float(Storage_Capacity.replace('GB', '').strip())
  else:
    return np.nan  # Handle unexpected formats

# Apply conversion function
df['Storage_Capacity'] = df['Storage_Capacity'].apply(convert_to_gb)

# Replace NaN values with 0 (for 'Not Available')
df['Storage_Capacity'] = df['Storage_Capacity'].fillna(0).astype('int32')

# Debugging: Print unique values after conversion
print("Unique values after conversion:", df['Storage_Capacity'].unique())
#checking the changes is done or not
print(df['Storage_Capacity'])
print("Unique values before conversion:", df['Storage_Capacity'].unique())

#storage type
df['Storage_Type']=df['Storage_Type'].replace(0,'Not Available')
df['Storage_Type']=df['Storage_Type'].fillna('Not Available')
df['Storage_Type']
#df.info()

#for operating system
df['Operating_System']=df['Operating_System'].replace(0,'Not Available')
df['Operating_System']=df['Operating_System'].fillna('Not Available')
df['Operating_System']

df['Prices'] = df['Prices'].astype(str).str.replace(',', '').str.strip()
df['Prices'] = pd.to_numeric(df['Prices'], errors='coerce')
df = df.dropna(subset=['Prices'])

df.head(20)
top_5_prices=df['Prices'].value_counts().nlargest(5)  #price 49990
plt.figure(figsize=(12, 6))
top_5_prices.plot(kind='bar')
plt.title('Frequency of Laptop Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')

# Display the plot
plt.show()

sns.displot(df['Prices'])
df.hist(figsize=(18,10))
plt.show()

plt.figure(figsize=(10, 7))
df['Brand'].value_counts().plot(kind='bar')
plt.show()

sns.barplot(x=df['Brand'],y=df['Prices'], palette='husl')
plt.xticks(rotation='vertical')     #taller bar willshow the highest average prices for that brand
plt.show()

sns.displot(df['Screen_Size_Inches'])

sns.scatterplot(x=df['Screen_Size_Inches'],y=df['Prices'])



sns.barplot(x=df['Operating_System'],y=df['Prices'], palette='husl')
plt.xticks(rotation='vertical')
plt.show()

df['Prices'] = pd.to_numeric(df['Prices'], errors='coerce')
df['Prices'].fillna(df['Prices'].median(), inplace=True) 

#spliting the dataset
X = df.drop(columns=['Prices'])
y = df['Prices']
print(y)
print(X)

# Split the data into training and testing sets (80% train, 20% test)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train)
print(X_test)
print(y_train)
print(y_test)
print(type(X_train))  
print(type(X_test))
print(type(y_test))  #y_train and y_test both are same




# Example Data Preparation (Assuming X_train, X_test, y_train, y_test are defined)
# Convert categorical features to string type for compatibility


# Identify categorical and numerical features
categorical_features = ['Brand', 'Processor_Type', 'Operating_System', 'Storage_Type']
numerical_features = ['Reviews', 'RAM_Size', 'Storage_Capacity', 'Screen_Size_Inches', 'Processor_Generation']
X_train[categorical_features] = X_train[categorical_features].astype(str)
X_test[categorical_features] = X_test[categorical_features].astype(str)
# Define the ColumnTransformer for preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),  # Scale numerical features
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)  # One-hot encode categorical features
    ])

# Create a pipeline that first preprocesses the data and then fits the model
pipeline = make_pipeline(preprocessor, Ridge(alpha=0.1))  # You can adjust alpha as needed

# Fit the pipeline to the training data
pipeline.fit(X_train, y_train)

# Make predictions
y_train_pred = pipeline.predict(X_train)  # Training predictions
y_val_pred = pipeline.predict(X_test)      # Validation predictions

# Calculate performance metrics
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("Training Performance:")
print("MAE:", mean_absolute_error(y_train, y_train_pred))
print("MSE:", mean_squared_error(y_train, y_train_pred))
print("R²:", r2_score(y_train, y_train_pred))

print("\nValidation Performance:")
print("MAE:", mean_absolute_error(y_test, y_val_pred))
print("MSE:", mean_squared_error(y_test, y_val_pred))
print("R²:", r2_score(y_test, y_val_pred))

# Learning Curve Calculation
train_sizes, train_scores, valid_scores = learning_curve(
    pipeline, X_train, y_train, cv=5, scoring='r2', train_sizes=np.linspace(0.1, 1.0, 10), random_state=42
)

# Calculate mean and standard deviation for training and validation scores
train_scores_mean = np.mean(train_scores, axis=1)
valid_scores_mean = np.mean(valid_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
valid_scores_std = np.std(valid_scores, axis=1)

# Plot Learning Curves
plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_scores_mean, label='Training Score', color='blue')
plt.plot(train_sizes, valid_scores_mean, label='Validation Score', color='orange')

# Add standard deviation shading
plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, color='blue', alpha=0.2)
plt.fill_between(train_sizes, valid_scores_mean - valid_scores_std, valid_scores_mean + valid_scores_std, color='orange', alpha=0.2)

# Add titles and labels
plt.title('Learning Curves')
plt.xlabel('Training Size')
plt.ylabel('R² Score')
plt.ylim(0, 1)  # Adjust based on your score range
plt.legend(loc='best')
plt.grid()
plt.show()

# displaying the 20 rows of the data table
df.head(20)
'''
#checking the model is fine or not
columns=['Reviews','Brand','Processor_Type','RAM_Size','Storage_Capacity','Storage_Type','Screen_Size_Inches','Operating_System','Processor_Generation']
input_data=pd.DataFrame([[4.2,'DELL',	'Intel Core i3',	8,	512,'SSD',	15.6,	'Windows 11',	12,]], columns=columns)  #sahi hai
input_data1= pd.DataFrame([[4.3,	'HP',	'AMD Ryzen 3',	8,	512,'SSD',	15.6,	'Windows 11',	0]], columns=columns)  #sahi hai littile bit
input_data2=pd.DataFrame([[4.0,	'Infinix',	'Intel Core i9',	32,	1024,'SSD',	15.6,	'Windows 11',	13]], columns=columns)
input_data3=pd.DataFrame([[4.1,	'MSI',	'AMD Ryzen 5'	,16,	512,'SSD',	15.6,	'Windows 11',	0]], columns=columns)
input_data4=pd.DataFrame([[4.3, 'Lenovo', 'AMD Ryzen 3', 8,512,'SSD',15.6, 'Windows 11', 0]], columns= columns) #sahi hai
input_data5=pd.DataFrame([[4.2, 'Lenovo', 'AMD Ryzen 7', 16,512,'SSD',15.6, 'Windows 11', 0]], columns= columns)
input_data6=pd.DataFrame([[3.9,	'ASUS',	'Intel Core i3'	,8,	512,'SSD',	15.6,	'Windows 11',	12]], columns= columns)#sahi hai
input_data7=pd.DataFrame([[4.3,'Acer','Intel Core i5',16,512,'SD',14.0,'Windows 11',13]],columns=columns)  #sahi hai
input_data8=pd.DataFrame([[4.3,'HP','AMR Ryzen 3',8,512,'SSD',15.6,'Windows 11',0]],columns=columns)
input_data9=pd.DataFrame([[4.2,'Primebook','Not Available',4,0,'Not Available',11.60,'Not Available',0]],columns=columns)
input_data10=pd.DataFrame([[4.4,'Infinix','Intel Core i5',16,512,'SSD',14,'Windows 11',13]],columns=columns)#sahi aaya hai
input_data11=pd.DataFrame([[4.3,'Infinix','Intel Core i9',32,1024,'SSD',16  ,'Windows 11',13]],columns=columns)#sahi aaya hai
input_data12=pd.DataFrame([[4.5,'samsung','Intel Core i3',8,512,'SSD',15.6  ,'Windows 11',13]],columns=columns)
input_data13=pd.DataFrame([[4.5,'samsung','Intel Core i5',8,512,'SSD',15.60  ,'Windows 11',13]],columns=columns)
input_data14 =pd.DataFrame([[4.5,'Lenovo', 'AMD Ryzen 5',16,512,'SSD',15.6  ,'Windows 11',0]],columns=columns)
# Transform the input data using the pipeline directly
predicted_price = pipeline.predict(input_data14)

# Round the predicted price
rounded_res = np.round(predicted_price, 2)
print(rounded_res)  # Print the result to see the output

'''

# Save the trained model (assuming your model is stored in the 'pipeline' variable)
joblib.dump(pipeline, 'D:/Laptop_interface/model_of_prediction.pkl')



