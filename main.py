import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import pandas as pd
import xml.etree.ElementTree as ET


def reverse_search_method(df):
    # Split the words into morphemes
    for index, row in df.iterrows():
        morphemes = row['word'].split()
        filename = '-'.join(morphemes) + '.md'
        connections = []
        # Loop the reversed morphemes to find possible phrases, then check their validity
        morphemes.reverse()
        for index in range(len(morphemes)):
            phrase_container = morphemes[0:index+1]
            phrase_container.reverse()
            phrase_container = '-'.join(phrase_container)
            connections.append(phrase_container)
        connections.pop()
        morphemes.reverse()
        with open(f"./VietnameseVault/{filename}", 'w') as file:
            file.write(f"# {row['word']}\n\n")
            file.write(f"## Definition:\n\n")
            file.write(f"{row['definition']}\n\n")
            file.write(f"Subwords:\n")
            for connection in connections:
                file.write(f"- [[{connection}]]\n")
        print(f"{filename} created - {index}")
    print("Done")

def parse_dictionary():
    tree = ET.parse('./resources/Viet_Anh.xml') 
    dictionary = tree.getroot()
    df = pd.DataFrame(columns=['word', 'definition'])
    # Only parsing first 100 while testing
    dictionary = dictionary[0:100]
    for record in dictionary:
        word_elm = record.find('word')
        definition_elm = record.find('meaning')
        if word_elm.text is not None and definition_elm is not None:
            word = word_elm.text.strip()
            definition = definition_elm.text.strip()
            df.loc[len(df.index)] = [word, definition]
    return df


def main():
    # Parse the dictionary to create a dataframe
    df = parse_dictionary()
    print(df.head())
    # Write data to markdown files
    reverse_search_method(df)

if __name__ == "__main__":
    main()