import os
import pandas as pd
from Controller.FirstAPI import GetRandomTenConsecutivePoints
from Controller.SecondAPI import PredictNextThreeValue

def ProcessStockFilesForExchange(exchangePath, numberFilesPerExchange):
    try:
        if not os.path.isdir(exchangePath):
            print(f"{exchangePath} is not a valid directory.")
            return  # Exit if the path is not a directory

        # Fetch available CSV files in the specific exchange folder
        csvFiles = [f for f in os.listdir(exchangePath) if f.endswith('.csv')]
        
        # Handle cases where there there are not enough files for exchange
        filesToProcess = csvFiles[:min(numberFilesPerExchange, len(csvFiles))]
        
        # Process each file
        for file in filesToProcess:
            print(f"Starting prediction for {file}")
            filePath = os.path.join(exchangePath, file)

            print("Get 10 consecutive data points...")
            # API 1: Get 10 consecutive data points from the CSV
            stockData = GetRandomTenConsecutivePoints(filePath)

            if stockData is None:
                continue  # Skip this file if there was an error
            
            print("Predict the next 3 stock prices...")
            # API 2: Predict the next 3 stock prices
            predictions = PredictNextThreeValue(stockData)
            
            if predictions is None:
                continue  # Skip in case of error
            
            # Combine the original data and predictions data
            result = pd.concat([stockData, predictions], ignore_index=True)
            
            # Save the result as a new CSV file
            outputFile = f"Data\\Output\\StockPredictions-{os.path.basename(filePath)}"
            result.to_csv(outputFile, index=False, header=False)
            print(f"Predictions saved to {outputFile}")
    
    except Exception as e:
        print(f"Error during processing: {e}")
