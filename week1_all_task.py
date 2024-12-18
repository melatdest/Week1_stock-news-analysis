# -*- coding: utf-8 -*-
"""Week1_all_task.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1z4WJBcPRA5-nHCEt1uuR6iwKzfAQ3ZZu
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import drive
# Mount your Google Drive
drive.mount('/content/drive')

# Once mounted, you can access your Drive files at '/content/drive/My Drive'
print("Drive mounted successfully!")

"""1. Load financial  Data"""

# Load datasets
raw_analyst_ratings = pd.read_csv('/content/drive/MyDrive/raw_analyst_ratings.csv/raw_analyst_rating.csv.csv') # corrected path to the actual CSV file
AAPL_historical_data = pd.read_csv('/content/drive/MyDrive/yfinance_data/yfinance_data/AAPL_historical_data.csv')
GOOG_historical_data = pd.read_csv('/content/drive/MyDrive/yfinance_data/yfinance_data/GOOG_historical_data.csv')
META_historical_data = pd.read_csv('/content/drive/MyDrive/yfinance_data/yfinance_data/META_historical_data.csv')
MSFT_historical_data = pd.read_csv('/content/drive/MyDrive/yfinance_data/yfinance_data/MSFT_historical_data.csv')
NVDA_historical_data = pd.read_csv('/content/drive/MyDrive/yfinance_data/yfinance_data/NVDA_historical_data.csv')
TSLA_historical_data = pd.read_csv('/content/drive/MyDrive/yfinance_data/yfinance_data/TSLA_historical_data.csv')

"""2. Perform Exploratory Data Analysis (EDA)

  Descriptive Statistics
"""

# List of datasets to process
datasets = {
    "raw_analyst_ratings": raw_analyst_ratings,
    "AAPL_historical_data": AAPL_historical_data,
    "GOOG_historical_data": GOOG_historical_data,
    "META_historical_data": META_historical_data,
    "MSFT_historical_data": MSFT_historical_data,
    "NVDA_historical_data": NVDA_historical_data,
    "TSLA_historical_data": TSLA_historical_data,
}

# Process each dataset
for name, df in datasets.items():
    if 'date' in df.columns:  # Check if 'date' column exists
        print(f"Processing datetime for {name}")
        # Convert 'date' column to datetime
        df['date'] = pd.to_datetime(df['date'], format='mixed', errors='coerce')

        # Handle invalid dates
        invalid_dates = df[df['date'].isnull()]
        if len(invalid_dates) > 0:
            print(f"{len(invalid_dates)} invalid dates found in {name}. Dropping invalid rows.")
            df.dropna(subset=['date'], inplace=True)
    else:
        print(f"No 'date' column in {name}. Skipping datetime processing.")

# Verify the results
for name, df in datasets.items():
    if 'date' in df.columns:
        print(f"First 5 dates in {name}:")
        print(df['date'].head())

# List of datasets
datasets = {
    "raw_analyst_ratings": raw_analyst_ratings,
    "AAPL_historical_data": AAPL_historical_data,
    "GOOG_historical_data": GOOG_historical_data,
    "META_historical_data": META_historical_data,
    "MSFT_historical_data": MSFT_historical_data,
    "NVDA_historical_data": NVDA_historical_data,
    "TSLA_historical_data": TSLA_historical_data
}

# EDA Results
eda_results = {}

for name, data in datasets.items():
    print(f"EDA for {name}:")

    # General info
    print("\n--- General Info ---")
    print(data.info())

    # Descriptive statistics for numeric columns
    print("\n--- Descriptive Statistics (Numeric) ---")
    print(data.describe())

    # Descriptive statistics for categorical columns
    print("\n--- Descriptive Statistics (Categorical) ---")
    categorical_data = data.select_dtypes(include=['object', 'category'])
    print(categorical_data.describe())

    # Missing values
    print("\n--- Missing Values ---")
    print(data.isnull().sum())

    # Correlation matrix (only for numeric columns)
    print("\n--- Correlation Matrix ---")
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    print(numeric_data.corr())

    # Store results for later access
    eda_results[name] = {
        "info": data.info(),
        "numeric_stats": data.describe(),
        "categorical_stats": categorical_data.describe(),
        "missing_values": data.isnull().sum(),
        "correlation_matrix": numeric_data.corr()
    }
    print("\n\n")

# Check the columns in GOOG_historical_data
print(GOOG_historical_data.columns)

# Check for the first few rows to identify relevant columns
print(GOOG_historical_data.head())

# Check the columns in GOOG_historical_data
print(META_historical_data.columns)

# Check for the first few rows to identify relevant columns
print(META_historical_data.head())

# Check the columns in GOOG_historical_data
print(MSFT_historical_data.columns)

# Check for the first few rows to identify relevant columns
print(MSFT_historical_data.head())

# Check the columns in GOOG_historical_data
print(NVDA_historical_data.columns)

# Check for the first few rows to identify relevant columns
print(NVDA_historical_data.head())

# Check the columns in GOOG_historical_data
print(TSLA_historical_data.columns)

# Check for the first few rows to identify relevant columns
print(TSLA_historical_data.head())

# Check the columns in each dataset to confirm the presence of 'headline_length' and 'publisher'
datasets = {
    "GOOG_historical_data": GOOG_historical_data,
    "META_historical_data": META_historical_data,
    "MSFT_historical_data": MSFT_historical_data,
    "NVDA_historical_data": NVDA_historical_data,
    "TSLA_historical_data": TSLA_historical_data
}

# Loop through datasets and print the columns
for dataset_name, data in datasets.items():
    print(f"Columns in {dataset_name}:")
    print(data.columns)
    print("="*50)

"""3. Sentiment Analysis
Use TextBlob for simplicity
"""

import matplotlib.pyplot as plt
import seaborn as sns

# Function to plot stock price distribution, volume distribution, and stock price trends
def plot_stock_data(data, ticker):
    # Set up the figure size for all plots
    plt.figure(figsize=(18, 6))

    # 1. Distribution of Closing Prices
    plt.subplot(1, 3, 1)
    sns.histplot(data['Close'], kde=True, color='blue')
    plt.title(f'{ticker} Stock Price Distribution')
    plt.xlabel('Price')
    plt.ylabel('Frequency')

    # 2. Distribution of Trading Volume
    plt.subplot(1, 3, 2)
    sns.histplot(data['Volume'], kde=True, color='green')
    plt.title(f'{ticker} Trading Volume Distribution')
    plt.xlabel('Volume')
    plt.ylabel('Frequency')

    # 3. Stock Price Trend (Close over Time)
    plt.subplot(1, 3, 3)
    data['Date'] = pd.to_datetime(data['Date'])  # Convert Date to datetime
    plt.plot(data['Date'], data['Close'], color='orange')
    plt.title(f'{ticker} Stock Price Trend')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')

    # Adjust layout to prevent overlapping of labels and titles
    plt.tight_layout()
    plt.show()

# Example of visualizations for each stock data

# Plot for GOOG_historical_data
plot_stock_data(GOOG_historical_data, 'GOOG')

# Plot for META_historical_data
plot_stock_data(META_historical_data, 'META')

# Plot for MSFT_historical_data
plot_stock_data(MSFT_historical_data, 'MSFT')

# Plot for NVDA_historical_data
plot_stock_data(NVDA_historical_data, 'NVDA')

# Plot for TSLA_historical_data
plot_stock_data(TSLA_historical_data, 'TSLA')

import matplotlib.pyplot as plt
import seaborn as sns

# Function to create the visualizations
def visualize_data(data, dataset_name):
    # Visualization for Headline Length Distribution
    if 'headline_length' in data.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(data['headline_length'], bins=50, kde=True)
        plt.title(f'Headline Length Distribution - {dataset_name}')
        plt.xlabel('Headline Length')
        plt.ylabel('Frequency')
        plt.show()

    # Visualization for Most Active Publisher
    if 'publisher' in data.columns:
        publisher_counts = data['publisher'].value_counts().head(10)  # Top 10 active publishers
        plt.figure(figsize=(10, 6))
        publisher_counts.plot(kind='bar', color='skyblue')
        plt.title(f'Most Active Publishers - {dataset_name}')
        plt.xlabel('Publisher')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45, ha='right')
        plt.show()

# Apply the visualizations to all datasets
for name, data in datasets.items():
    visualize_data(data, name)

from textblob import TextBlob

# Perform sentiment analysis
def get_sentiment_score(headline):
    analysis = TextBlob(headline)
    return analysis.sentiment.polarity

raw_analyst_ratings['sentiment_score'] = raw_analyst_ratings['headline'].apply(get_sentiment_score)

# Visualize sentiment distribution
sns.histplot(raw_analyst_ratings['sentiment_score'], bins=30, kde=True)
plt.title('Distribution of Sentiment Scores')
plt.show()

"""4. Correlation Analysis

Align dates and calculate stock movements
"""

# Commented out IPython magic to ensure Python compatibility.
!wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
!tar -xzvf ta-lib-0.4.0-src.tar.gz
# %cd ta-lib
!./configure --prefix=/usr
!make
!make install
!pip install TA-Lib

import talib

# Add a technical indicator
AAPL_historical_data['SMA_20'] = talib.SMA(AAPL_historical_data['Close'], timeperiod=20)
AAPL_historical_data['RSI'] = talib.RSI(AAPL_historical_data['Close'], timeperiod=14)

# Visualize indicators
plt.figure(figsize=(10, 6))
plt.plot(AAPL_historical_data['date'], AAPL_historical_data['Close'], label='Close Price')
plt.plot(AAPL_historical_data['date'], AAPL_historical_data['SMA_20'], label='SMA 20')
plt.title('AAPL Close Price and SMA')
plt.legend()
plt.show()

AAPL_historical_data['date'] = pd.to_datetime(AAPL_historical_data['Date'])

# Convert both date columns to UTC
raw_analyst_ratings['date'] = pd.to_datetime(raw_analyst_ratings['date']).dt.tz_convert('UTC')
AAPL_historical_data['date'] = pd.to_datetime(AAPL_historical_data['Date']).dt.tz_localize('UTC')

# Now merge the datasets
news_stock_data = pd.merge(
    raw_analyst_ratings,
    AAPL_historical_data[['date', 'Close']],
    on='date',
    how='inner'
)

# Normalize date and align data (convert both to UTC)
raw_analyst_ratings['date'] = pd.to_datetime(raw_analyst_ratings['date']).dt.tz_convert('UTC')
GOOG_historical_data['date'] = pd.to_datetime(GOOG_historical_data['Date']).dt.tz_localize('UTC')

# Now merge the datasets
news_stock_data = pd.merge(
    raw_analyst_ratings,
    GOOG_historical_data[['date', 'Close']],
    on='date',
    how='inner'
)

# Calculate daily returns
news_stock_data['daily_return'] = news_stock_data['Close'].pct_change()

# Aggregate sentiment scores
daily_sentiment = news_stock_data.groupby('date')['sentiment_score'].mean().reset_index()

# Merge with daily returns
correlation_data = pd.merge(
    daily_sentiment,
    news_stock_data[['date', 'daily_return']],
    on='date'
)

# Calculate Pearson correlation
correlation = correlation_data['sentiment_score'].corr(correlation_data['daily_return'])
print(f"Correlation between sentiment and daily returns for GOOG: {correlation}")

print(correlation_data['sentiment_score'].nunique())  # Number of unique sentiment scores
print(correlation_data['daily_return'].nunique())  # Number of unique daily returns

print(correlation_data.isna().sum())



print(raw_analyst_ratings['date'].head())
print(AAPL_historical_data['date'].head())

news_stock_data = pd.merge(
    raw_analyst_ratings,
    AAPL_historical_data[['date', 'Close']],
    on='date',
    how='outer',  # This will keep all rows from both dataframes
    indicator=True  # Adds a column to show where the merge matched
)
print(news_stock_data['_merge'].value_counts())

# Filter the date range for both datasets (e.g., 2020-2024)
raw_analyst_ratings = raw_analyst_ratings[raw_analyst_ratings['date'] >= '2020-01-01']
AAPL_historical_data = AAPL_historical_data[AAPL_historical_data['date'] >= '2020-01-01']

# Now try merging again
news_stock_data = pd.merge(
    raw_analyst_ratings,
    AAPL_historical_data[['date', 'Close']],
    on='date',
    how='inner'
)
print(news_stock_data.shape)

common_start_date = max(raw_analyst_ratings['date'].min(), AAPL_historical_data['date'].min())
common_end_date = min(raw_analyst_ratings['date'].max(), AAPL_historical_data['date'].max())

print(f"Common date range: {common_start_date} to {common_end_date}")

# Filter both datasets based on the common date range
raw_analyst_ratings = raw_analyst_ratings[(raw_analyst_ratings['date'] >= common_start_date) & (raw_analyst_ratings['date'] <= common_end_date)]
AAPL_historical_data = AAPL_historical_data[(AAPL_historical_data['date'] >= common_start_date) & (AAPL_historical_data['date'] <= common_end_date)]

# Now try merging again
news_stock_data = pd.merge(
    raw_analyst_ratings,
    AAPL_historical_data[['date', 'Close']],
    on='date',
    how='inner'
)
print(news_stock_data.shape)

news_stock_data = pd.merge(
    raw_analyst_ratings,
    AAPL_historical_data[['date', 'Close']],
    on='date',
    how='left'
)

# Convert both 'date' columns to just the date (ignoring time)
raw_analyst_ratings['date'] = raw_analyst_ratings['date'].dt.date
AAPL_historical_data['date'] = AAPL_historical_data['date'].dt.date

# Re-merge the datasets
news_stock_data = pd.merge(
    raw_analyst_ratings,
    AAPL_historical_data[['date', 'Close']],
    on='date',
    how='inner'
)

print(news_stock_data.shape)

print(f"Common date range after stripping time: {raw_analyst_ratings['date'].min()} to {raw_analyst_ratings['date'].max()}")

# Calculate daily returns
news_stock_data['daily_return'] = news_stock_data['Close'].pct_change()

# Aggregate sentiment scores
daily_sentiment = news_stock_data.groupby('date')['sentiment_score'].mean().reset_index()

# Merge with daily returns
correlation_data = pd.merge(
    daily_sentiment,
    news_stock_data[['date', 'daily_return']],
    on='date'
)

# Calculate Pearson correlation
correlation = correlation_data['sentiment_score'].corr(correlation_data['daily_return'])
print(f"Correlation between sentiment and daily returns: {correlation}")



import matplotlib.pyplot as plt

# Plot daily returns
plt.figure(figsize=(10, 5))
plt.plot(correlation_data['date'], correlation_data['daily_return'], label='Daily Returns')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.title('Daily Returns Over Time')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Plot sentiment scores
plt.figure(figsize=(10, 5))
plt.plot(correlation_data['date'], correlation_data['sentiment_score'], label='Sentiment Score', color='orange')
plt.xlabel('Date')
plt.ylabel('Sentiment Score')
plt.title('Sentiment Score Over Time')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Check for missing values
print("Missing values in sentiment_score:", correlation_data['sentiment_score'].isnull().sum())
print("Missing values in daily_return:", correlation_data['daily_return'].isnull().sum())

# Check for constant values
print("Unique values in sentiment_score:", correlation_data['sentiment_score'].nunique())
print("Unique values in daily_return:", correlation_data['daily_return'].nunique())

# Drop rows with NaN values
correlation_data = correlation_data.dropna(subset=['sentiment_score', 'daily_return'])

# Recalculate the Pearson correlation after cleaning
correlation = correlation_data['sentiment_score'].corr(correlation_data['daily_return'])
print(f"Correlation between sentiment and daily returns: {correlation}")

# Normalize date and align data (convert both to UTC)
raw_analyst_ratings['date'] = pd.to_datetime(raw_analyst_ratings['date']).dt.tz_localize('UTC')
MSFT_historical_data['date'] = pd.to_datetime(MSFT_historical_data['Date']).dt.tz_localize('UTC')
NVDA_historical_data['date'] = pd.to_datetime(NVDA_historical_data['Date']).dt.tz_localize('UTC')
TSLA_historical_data['date'] = pd.to_datetime(TSLA_historical_data['Date']).dt.tz_localize('UTC')

# Merge the datasets
def calculate_correlation(stock_data, stock_name):
    stock_data = pd.merge(
        raw_analyst_ratings,
        stock_data[['date', 'Close']],
        on='date',
        how='inner'
    )

    # Calculate daily returns
    stock_data['daily_return'] = stock_data['Close'].pct_change()

    # Aggregate sentiment scores
    daily_sentiment = stock_data.groupby('date')['sentiment_score'].mean().reset_index()

    # Merge with daily returns
    correlation_data = pd.merge(
        daily_sentiment,
        stock_data[['date', 'daily_return']],
        on='date'
    )

    # Drop missing values
    correlation_data = correlation_data.dropna(subset=['daily_return'])

    # Calculate Pearson correlation
    correlation = correlation_data['sentiment_score'].corr(correlation_data['daily_return'])
    print(f"Correlation between sentiment and daily returns for {stock_name}: {correlation}")

# Apply to MSFT, NVDA, TSLA
calculate_correlation(MSFT_historical_data, "MSFT")
calculate_correlation(NVDA_historical_data, "NVDA")
calculate_correlation(TSLA_historical_data, "TSLA")

def calculate_correlation_and_plot(stock_data, stock_name):
    # Merge the datasets
    stock_data = pd.merge(
        raw_analyst_ratings,
        stock_data[['date', 'Close']],
        on='date',
        how='inner'
    )

    # Check if sentiment_score column exists after merge
    if 'sentiment_score' not in stock_data.columns:
        print(f"Sentiment score column is missing for {stock_name}")
        return

    # Calculate daily returns
    stock_data['daily_return'] = stock_data['Close'].pct_change()

    # Aggregate sentiment scores
    daily_sentiment = stock_data.groupby('date')['sentiment_score'].mean().reset_index()

    # Merge with daily returns
    correlation_data = pd.merge(
        daily_sentiment,
        stock_data[['date', 'daily_return']],
        on='date'
    )

    # Drop missing values
    correlation_data = correlation_data.dropna(subset=['daily_return'])

    # Calculate Pearson correlation
    correlation = correlation_data['sentiment_score'].corr(correlation_data['daily_return'])
    print(f"Correlation between sentiment and daily returns for {stock_name}: {correlation}")

    # Plotting the data
    plt.figure(figsize=(10, 6))
    plt.scatter(correlation_data['sentiment_score'], correlation_data['daily_return'], alpha=0.5)
    plt.title(f"Sentiment vs Daily Returns for {stock_name}")
    plt.xlabel("Sentiment Score")
    plt.ylabel("Daily Return")
    plt.grid(True)
    plt.show()

# Apply to MSFT, NVDA, TSLA
calculate_correlation_and_plot(MSFT_historical_data, "MSFT")
calculate_correlation_and_plot(NVDA_historical_data, "NVDA")
calculate_correlation_and_plot(TSLA_historical_data, "TSLA")