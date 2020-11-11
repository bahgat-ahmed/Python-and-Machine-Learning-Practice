# Display the number of rows and columns
nsfg.shape

# Display the names of the columns
nsfg.columns

# Select column birthwgt_oz1: ounces
ounces = nsfg['birthwgt_oz1']

# Print the first 5 elements of ounces
print(ounces[:5])

# How many pregnancies in this dataset ended with a live birth?
nsfg['nbrnaliv'].value_counts()

# Replace the value 8 with NaN
nsfg['nbrnaliv'].replace(8, np.nan, inplace=True)

# Print the values and their frequencies
print(nsfg['nbrnaliv'].value_counts())

# A variable that's computed from other variables is sometimes called a 'recode'

# Select the columns and divide by 100
agecon = nsfg['agecon'] / 100
agepreg = nsfg['agepreg'] / 100

# Compute the difference
preg_length = agepreg - agecon

# Compute summary statistics
print(preg_length.describe())

# Plot the histogram (Adapt your code to make an unfilled histogram by setting the parameter histtype to be 'step')
plt.hist(agecon, bins=20, histtype='step')

# Label the axes
plt.xlabel('Age at conception')
plt.ylabel('Number of pregnancies')

# Show the figure
plt.show()

# Resample the data
nsfg = resample_rows_weighted(nsfg, 'wgt2013_2015')

# Clean the weight variables
pounds = nsfg['birthwgt_lb1'].replace([98, 99], np.nan)
ounces = nsfg['birthwgt_oz1'].replace([98, 99], np.nan)

# Compute total birth weight
birth_weight = pounds + ounces/16

# Create a Boolean Series for full-term babies
full_term = nsfg['prglngth'] >= 37

# Select the weights of full-term babies
full_term_weight = birth_weight[full_term]

# Compute the mean weight of full-term babies
print(np.mean(full_term_weight))

# Filter full-term babies
full_term = nsfg['prglngth'] >= 37

# Filter single births
single = nsfg['nbrnaliv'] == 1

# Compute birth weight for single full-term babies
single_full_term_weight = birth_weight[single & full_term]
print('Single full-term mean:', single_full_term_weight.mean())

# Compute birth weight for multiple full-term babies
mult_full_term_weight = birth_weight[~single & full_term]
print('Multiple full-term mean:', mult_full_term_weight.mean())

# the PMF shows all unique values, so we can exactly where the peaks are. However, since the historgram puts values into bins, it obscures some details PMFs have limitations too

# Compute the PMF for year
pmf_year = Pmf(gss['year'], normalize=False)

# Print the result
print(pmf_year)

# Select the age column
age = gss['age']

# Make a PMF of age
pmf_age = Pmf(age)

# Plot the PMF
pmf_age.bar()

# You could also use pmf_age.plot() to plot the Pmf as a line plot

# Label the axes
plt.xlabel('Age')
plt.ylabel('PMF')
plt.show()

# Select the age column
age = gss['age']

# Compute the CDF of age
cdf_age = Cdf(age)

# Calculate the CDF of 30
print(cdf_age(30))

# Recall from the video that the interquartile range (IQR) is the difference between the 75th and 25th percentiles. Because IQR (Inter Quartile Range) is based on percentiles, it doesn't get thrown off by extreme values or outliers, the way variance does.

# Calculate the 75th percentile
percentile_75th = cdf_income.inverse(0.75)

# Calculate the 25th percentile
percentile_25th = cdf_income.inverse(0.25)

# Calculate the interquartile range
iqr = percentile_75th - percentile_25th

# Print the interquartile range
print(iqr)

# Select realinc
income = gss['realinc']

# Make the CDF
cdf_income = Cdf(income)

# Plot it
cdf_income.plot()

# Label the axes
plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.show()

# In general, CDFs are smoother than PMFs because they smooth out randomness, we can often get a better view of real differences between distributions

# Remember, you can use logical operators to make Boolean Series and select rows from a DataFrame or Series

# Select educ
educ = gss['educ']

# Bachelor's degree
bach = (educ >= 16)

# Associate degree
assc = (educ >= 14) & (educ < 16)

# High school (12 or fewer years of education)
high = (educ <= 12)
print(high.mean())

income = gss['realinc']

# Plot the CDFs
Cdf(income[high]).plot(label='High school')
Cdf(income[assc]).plot(label='Associate')
Cdf(income[bach]).plot(label='Bachelor')

# Label the axes
plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.legend()
plt.show()

# we saw that PMF don't work very well when the data have a large number of unique values

# Kernel Density Estimation (KDE): It is a way of getting from PMF to PDF (Probability Density Function). This can happen by using the points in the sample to estimate the PDF of the distribution they came from

# PDFs is a more sensitive way to look for differences, but often ut is too sensitive. It's hard to tell whether apparent differences mean anything, or if they are just random

# CDFs for exploration. They give the best view of what's going on without getting distracted by noise. Their biggest drawback is that they are less well known. So, you can use instead PMFs and KDEs if the audience is unfamiliar with CDFs
