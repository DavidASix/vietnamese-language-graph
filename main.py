import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import pandas as pd
import xml.etree.ElementTree as ET


def dict_match_search_method(df):
    df['morpheme_count'] = df['word'].str.split().str.len()
    for i, row in df.iterrows():
        sub_words = []
        # Iterate the possible lengths of subwords, and compare all possible subwords of current word against df of all subwords at the same length
        possible_subword_morpheme_lengths = [x for x in range(1, row['morpheme_count'])]
        for l in possible_subword_morpheme_lengths:
            possible_sub_words = df[df['morpheme_count'] == l]
            possible_sub_words = possible_sub_words['kebab'].tolist()
            morphemes = row['kebab'].split('-')
            # Split the morphemes and compare all combinations of the current possible subword length while maintaining order
            for j in range(len(morphemes) - l + 1):
                sub_word = '-'.join(morphemes[j:j+l])
                if sub_word in possible_sub_words:
                    sub_words.append(sub_word)

        # Write result to markdown file
        filename = row['kebab'] + '.md'
        write_markdown_file({
            'filename': filename, 
            'word': row['word'], 
            'definition': row['definition'], 
            'connections': sub_words})


# This is the original method to create the markdown files
def reverse_search_method(df):
    # Split the words into morphemes
    for i, row in df.iterrows():
        morphemes = row['word'].split()
        filename = row['kebab'] + '.md'
        connections = []
        # Loop the reversed morphemes to find possible phrases, then check their validity
        morphemes.reverse()
        for j in range(len(morphemes)):
            phrase_container = morphemes[0:j+1]
            phrase_container.reverse()
            phrase_container = '-'.join(phrase_container)
            connections.append(phrase_container)
        connections.pop()
        morphemes.reverse()
        write_markdown_file({
            'filename': filename, 
            'word': row['word'], 
            'definition': row['definition'], 
            'connections': connections})
    print("Done")

def parse_dictionary():
    tree = ET.parse('./resources/Viet_Anh.xml') 
    dictionary = tree.getroot()
    df = pd.DataFrame(columns=['word', 'kebab', 'definition'])
    print('Parsing Dictionary...')
    # Only parsing first 100 while testing
    #dictionary = dictionary[0:100]
    for record in dictionary:
        word_elm = record.find('word')
        definition_elm = record.find('meaning')
        if word_elm.text is not None and definition_elm is not None:
            word = word_elm.text.strip()
            kebab = word_elm.text.strip().split()
            kebab = '-'.join(kebab)
            definition = definition_elm.text.strip()
            df.loc[len(df.index)] = [word, kebab, definition]
    print(f"Dictionary parsed - {len(df.index)} entries")
    return df

def write_markdown_file(md_file):
    with open(f"./ObsidianVault/{md_file['filename']}", 'w') as file:
        file.write(f"# {md_file['word']}\n\n")
        file.write(f"## Definition:\n\n")
        file.write(f"{md_file['definition']}\n\n")
        file.write(f"## Subwords:\n")
        for connection in md_file['connections']:
            file.write(f"- [[{connection}]]\n")
    print(f"{md_file['filename']} created")

def main():
    # Parse the dictionary to create a dataframe
    df = parse_dictionary()
    # Write data to markdown files
    dict_match_search_method(df)

if __name__ == "__main__":
    main()