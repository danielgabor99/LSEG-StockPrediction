import git
import os
from Utils.FileProcessor import ProcessStockFilesForExchange

def getProjectRoot():
    return git.Repo('.', search_parent_directories=True).working_tree_dir


if __name__ == "__main__":
    project_root = getProjectRoot()

    # Define the path to the specific stock exchange folder relative to the project root
    ExchangeFolder = os.path.join(project_root, "Data", "stock_price_data_files", "NASDAQ")
    NumberOfFiles = int(input("Please enter the number of files (1 or 2): ")) # Number of files to sample from the specified exchange folder
    
    ProcessStockFilesForExchange(ExchangeFolder, NumberOfFiles)