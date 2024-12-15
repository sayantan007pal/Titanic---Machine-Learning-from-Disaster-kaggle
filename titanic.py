import pandas as pd
import matplotlib.pyplot as plt

# Load the train dataset
train_df = pd.read_csv('train.csv')

# Prepare data for analysis
train_df['AgeGroup'] = pd.cut(train_df['Age'], bins=[0, 12, 18, 35, 60, 80], labels=['Child', 'Teen', 'Young Adult', 'Adult', 'Senior'])

# Compute survival statistics
survival_rate = train_df['Survived'].value_counts(normalize=True)
survival_by_gender = train_df.groupby('Sex')['Survived'].mean()
survival_by_class = train_df.groupby('Pclass')['Survived'].mean()
survival_by_age_group = train_df.groupby('AgeGroup')['Survived'].mean()
survival_by_embarkation = train_df.groupby('Embarked')['Survived'].mean()

# Save results to CSV
survival_rate.to_csv('overall_survival_rate.csv', header=['Proportion'])
survival_by_gender.to_csv('survival_by_gender.csv', header=['Survival Rate'])
survival_by_class.to_csv('survival_by_class.csv', header=['Survival Rate'])
survival_by_age_group.to_csv('survival_by_age_group.csv', header=['Survival Rate'])
survival_by_embarkation.to_csv('survival_by_embarkation.csv', header=['Survival Rate'])

# Plot visualizations
# Overall Survival Rate
plt.figure(figsize=(8, 5))
train_df['Survived'].value_counts(normalize=True).plot(kind='bar', color=['skyblue', 'orange'])
plt.title('Overall Survival Rate')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Proportion')
plt.xticks(rotation=0)
plt.savefig('overall_survival_rate.png')
plt.show()

# Survival by Gender
plt.figure(figsize=(8, 5))
survival_by_gender.plot(kind='bar', color=['lightcoral', 'lightblue'])
plt.title('Survival Rate by Gender')
plt.xlabel('Gender')
plt.ylabel('Survival Rate')
plt.xticks(rotation=0)
plt.savefig('survival_by_gender.png')
plt.show()

# Survival by Class
plt.figure(figsize=(8, 5))
survival_by_class.plot(kind='bar', color=['gold', 'silver', 'brown'])
plt.title('Survival Rate by Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.xticks(rotation=0)
plt.savefig('survival_by_class.png')
plt.show()

# Survival by Age Group
plt.figure(figsize=(8, 5))
survival_by_age_group.plot(kind='bar', color='orchid')
plt.title('Survival Rate by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Survival Rate')
plt.xticks(rotation=45)
plt.savefig('survival_by_age_group.png')
plt.show()

# Survival by Embarkation Port
plt.figure(figsize=(8, 5))
survival_by_embarkation.plot(kind='bar', color=['teal', 'navy', 'purple'])
plt.title('Survival Rate by Embarkation Port')
plt.xlabel('Embarkation Port')
plt.ylabel('Survival Rate')
plt.xticks(rotation=0)
plt.savefig('survival_by_embarkation.png')
plt.show()
