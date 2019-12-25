# gb_text = "I realise I can see the world in colour but I can't vocalise its splendour"
# us_text = replace_all(gb_text, us2gb)
# print ("GB:", gb_text)
# print ("----------------------------------------------------------------------------")
# print ("US:", us_text)

# key/value pairs can be added if required

import pandas as pd
us2gb = pd.read_csv('./gb_us_eng_spell.csv',header=None)
us2gb.set_index(0,inplace=True)
us2gb = us2gb.iloc[:,0].to_dict()

def replace_gb2us(text, mydict=None):
    '''
    Replace words in British English spelling with American English spelling.
    '''
    if mydict == None:
        mydict = us2gb
        
    for gb, us in mydict.items():
        text = text.replace(us, gb)
    return text

def replace_us2gb(text, mydict=None):
    '''
    Replace words in British English spelling with American English spelling.
    '''
    if mydict == None:
        mydict = us2gb
    
    for gb, us in mydict.items():
        text = text.replace(gb,us)
    return text