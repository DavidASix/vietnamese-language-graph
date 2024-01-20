import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import pandas as pd
import xml.etree.ElementTree as ET

def main():
    # Parse the dictionary to create a dataframe
    tree = ET.parse('./resources/Viet_Anh.xml') 
    dictionary = tree.getroot()
    df = pd.DataFrame(columns=['word', 'definition'])
    # Only parsing first 100 while testing
    for record in dictionary[0:100]:
        word_elm = record.find('word')
        definition_elm = record.find('meaning')
        if word_elm.text is not None and definition_elm is not None:
            word = word_elm.text.strip()
            definition = definition_elm.text.strip()
            df.loc[len(df.index)] = [word, definition]  
    print(df.head())

if __name__ == "__main__":
    main()