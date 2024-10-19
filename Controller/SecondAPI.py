import pandas as pd
from datetime import datetime, timedelta

def PredictNextThreeValue(stockData):
    try:
        if stockData is None or len(stockData) < 10:
            raise ValueError("Insufficient data for prediction")
        # Extract the stock prices from the selected data
        
        # Access the stock price column (3rd column, index 2)
        prices = stockData.iloc[:, 2].values
        
        # Calculate the predictions
        n1 = round(sorted(prices)[-2], 2)  # 2nd highest value rounded to 2 decimals
        n2 = round(prices[-1] + 0.5 * (n1 - prices[-1]), 2)
        n3 = round(n2 + 0.25 * (n1 - n2), 2)

        lastTimestamp = stockData.iloc[-1, 1]  # Assuming the timestamp is in the 2nd column (index 1)
        lastDate = datetime.strptime(lastTimestamp, '%d-%m-%Y')

        # Calculate predicted timestamps
        predictedTimestamps = [
            (lastDate + timedelta(days=i)).strftime('%d-%m-%Y') for i in range(1, 4)
        ]

        # Create a DataFrame to store the predictions
        predictedData = pd.DataFrame({
            0: stockData.iloc[:, 0].repeat(3).reset_index(drop=True)[:3],
            1: predictedTimestamps,
            2: [n1, n2, n3]
        })
        
        return predictedData
    
    except Exception as e:
        print(f"Error in prediction: {e}")
        return None
