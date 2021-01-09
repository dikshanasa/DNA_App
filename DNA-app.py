#importing libraries
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
#Page title
image = Image.open('dna-logo.jpg')
st.image(image,use_column_width=True)
st.write("""
#DNA Nucleotide Count Web App

This app counts the nucleotide compositions of query DNA!
***
""")
#Input Text Box
st.header ('Enter DNA Sequence')
Sequence_input=">DNA query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence=st.text_area("Sequence Input",Sequence_input,height=250)
sequence=sequence.splitlines()
sequence=sequence[1:]
sequence=''.join(sequence)
st.write("""
***
""")
st.header('INPUT (DNA Query)')
sequence
#DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')
#Print dictionary
st.subheader('1.Print Dictionary')
def DNA_Nucleotide_count(seq):
    d=dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C')),

    ])
    return d
X= DNA_Nucleotide_count(sequence)
X
st.subheader('2.Print Text')
st.write('There are '+str(X['A']) + ' adenine (A)')
st.write('There are '+str(X['T']) + ' adenine (T)')
st.write('There are '+str(X['G']) + ' adenine (G)')
st.write('There are '+str(X['C']) + ' adenine (C)')
### 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)
#Display Bar Chart
st.subheader('4.Display Bar Chart')
p=alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
    
)
p=p.properties(
    width=alt.Step(80),
       
)
st.write(p)

