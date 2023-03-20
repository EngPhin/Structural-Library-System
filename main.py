import os
import GUI
from selection_class import DocumentSelectionMetadata as DSM

def main():
    selection_data = GUI.mainWindow()
    
    return selection_data

if __name__ == "__main__":
    data = main()
    print(data.document_type)
