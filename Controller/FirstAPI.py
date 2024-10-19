import pandas as pd
import random

def GetRandomTenConsecutivePoints(filePath):
    try:
        data = pd.read_csv(filePath, header=None)
        if data.empty:
            raise ValueError("Empty file")
        
        # Ensure that there are enough rows in the file
        if len(data) < 10:
            raise ValueError("Not enough data points in the file")
        
        # Random starting point
        startIndex = random.randint(0, len(data) - 10)
        selectedData = data.iloc[startIndex:startIndex + 10]
        
        return selectedData
    
    except Exception as e:
        print(f"Error in processing file {filePath}: {e}")
        return None