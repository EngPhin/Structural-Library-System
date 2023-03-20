import tkinter as tk
from tkinter import ttk
from tkinter import Grid
from selection_class import DocumentSelectionMetadata as DSM

selection_info =DSM(title_entry="n/a",
                    filename_entry="n/a",
                    publisher_options="n/a",
                    structure_options="n/a",
                    document_options="n/a")

def mainWindow():
    # create a new window
    window = tk.Tk()

    # set the window title
    window.title("Document Selection")
    window.geometry("500x500")

    # create a function to handle the selection
    def select_info():
        # get the selected options
        title = title_entry.get()
        filename = filename_entry.get()
        publisher = publisher_options.get()
        structure_type = structure_options.get()
        document_type = document_options.get()
        
        selection_info.title=title
        selection_info.filename=filename
        selection_info.publisher=publisher
        selection_info.structure_type=structure_type
        selection_info.document_type=document_type
        
        # print the selected options
        print("Title:", title)
        print("Filename:", filename)        
        print("Publisher:", publisher)
        print("Type of Structure:", structure_type)
        print("Type of Document:", document_type)
    
    # create labels and entry boxes for each option
    filename_label = ttk.Label(window, text="Filename: ")
    filename_entry = ttk.Entry(window)

    title_label = ttk.Label(window, text="Title: ")
    title_entry = ttk.Entry(window)

    publisher_label = ttk.Label(window, text="Publisher", anchor="w")
    publisher_options = ttk.Combobox(window, values=["Eurocode", "ACI", "AISC", "ASCE", "HK CoP", "Others"])

    structure_label = ttk.Label(window, text="Type of Structure")
    structure_options = ttk.Combobox(window, values=["Buildings", "Bridges", "Culverts", "Others"])

    document_label = ttk.Label(window, text="Type of Document")
    document_options = ttk.Combobox(window, values=["Book", "Journal/Paper", "Design Code/Standard", "Design Guide", "Specification", "Others"])

    # create a button to submit the selection
    submit_button = ttk.Button(window, text="Submit", command=select_info)

    # create a button to exit
    exit_button = ttk.Button(window, text="Exit",command=window.destroy)


    # use grid geometry manager to arrange the widgets in a grid
    filename_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    filename_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    title_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    title_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    publisher_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    publisher_options.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    structure_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    structure_options.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    document_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
    document_options.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    submit_button.grid(row=5, column=1, padx=5, pady=5, sticky="e")
    exit_button.grid(row=6, column=1, padx=5, pady=5, sticky="e")

    # run the main event loop
    window.mainloop()
    
    return selection_info

if __name__ == "__main__":
    mainWindow()