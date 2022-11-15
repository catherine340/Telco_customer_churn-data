# reading the file
import  numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_excel("dataset.xlsx")
print(df)

print(df.shape)

#Distribution of the churn data in this dataset
print(df['Churn Label'].value_counts())


sns.countplot(x='Churn Label',data=df,color='grey')
plt.title('churn count')
plt.xlabel('Churn Label')
plt.ylabel('Total count')
plt.show()

# read the file and explain data types statistically as well as how python is reading it. Please let us know if any data type is read wrong.
print(df.dtypes)

df['Total Charges'] = pd.to_numeric(df['Total Charges'],errors='coerce')
print(df.dtypes)

#apply appropriate statistical measures using python based on data types.
print(df.head(5))

print(df.mean())
print(df.median())

#mode()
print(df['Longitude'].mode(),
      df['Payment Method'].mode(),
      df['Gender'].mode(),
      df['Paperless Billing'].mode(),
      df['Contract'].mode(),
      df['Internet Service'].mode(),
      df['Monthly Charges'].mode(),
      df['Total Charges'].mode(),
      df['Churn Label'].mode())

#Standard deviation()
print(df.std())

#VARIANCE
print(df.var())

#IQR-INTER QUARTILE RANGE
q75, q25 = np.percentile(df['Tenure Months'], [75 ,25])
iqr = q75 - q25
print(iqr)

q75, q25 = np.percentile(df['Monthly Charges'], [75 ,25])
iqr = q75 - q25
print(iqr)

q75, q25 = np.percentile(df['Churn Score'], [75 ,25])
iqr = q75 - q25
print(iqr)

q75, q25 = np.percentile(df['CLTV'], [75 ,25])
iqr = q75 - q25
print(iqr)

#Max()
print(df.max())

#Min()
print(df.min())

#What is the percentage of females and senior citizens in this data set? Please create appropriate plots and explain the plots.
#Counting total numbers in each category
count=df['Gender'].value_counts()
#checking the numbers
print(count)
#creating the categories
ChurnLabel = ['Male','Female']
#creating plot
fig = plt.figure()
#show plot
plt.pie(count,labels = ChurnLabel,autopct='%1.1f%%',shadow=True,startangle=90,colors=('red','lavender'))
plt.title("Pie Chart-GENDER")
plt.show()

#Counting total numbers in each category
count=df['Senior Citizen'].value_counts()
#checking the numbers
print(count)
#creating the categories
ChurnLabel = ['Not senior citizens','Senior Citizens']
#creating plot
fig = plt.figure()
#show plot
plt.pie(count,labels = ChurnLabel,autopct='%1.1f%%',shadow=True,startangle=90,colors=('orange','turquoise'))
plt.title("Pie Chart-percentage of senior citizens")
plt.show()

#create an appropriate plot to examine the distribution of the tenure month column and explain the distribution. Based on distribution, perform appropriate statistical measures.
plt.hist(df["Tenure Months"],color='green')
plt.title("Tenure Months - Histogram plot")
plt.xlabel("Tenure")
plt.ylabel("Customers")
plt.grid(True)
plt.show()

#examine the distribution of monthly charges between males and females using box plots
sns.boxplot(x='Gender',y='Monthly Charges',data=df,color='teal')
plt.show()

sns.boxplot(x='Gender',y='Monthly Charges',hue='Churn Label',data=df,color='blue')
plt.show()

#find which payment method has the highest churn score and which has the lowest churn score.
print(df.sort_values(by='Churn Score',ascending=True))
print(df.sort_values(by='Churn Score',ascending=False))

#create an appropriate plot to check the count of payment methods and explain it.
sns.countplot(x='Payment Method',data=df,color='black')
plt.title('Count plot-payment method')
plt.xlabel('Payment Method')
plt.ylabel('Total Count')
plt.show()

#create an appropriate plot to see the relationship between monthly charges and total charges.
sns.scatterplot(x="Monthly Charges",y="Total Charges",data=df,color='salmon')
plt.show()

sns.scatterplot(x="Monthly Charges",y="Total Charges",hue="Churn Value",data=df)
plt.show()











