# Article trend Analysis by word2vec

### Summary
This Jupyter Notebook demonstrates application example of NLP to energy-industry articles in PDF. <br>

### Part1: Preprocessing
Preprocessing part is described: conversion from PDF to text, tokenizer, duplicate file deletion. <br>
About 600 articles were collected and converted into text files. <br>
https://github.com/Jun-Tam/article_analysis_word2vec/blob/master/NLP_Articles_Preprocess.ipynb


### Part2: Trend Analysis
Analysis part is described: BoW, IDF/TF, word2vec, WordCloud <br>
https://github.com/Jun-Tam/article_analysis_word2vec/blob/master/NLP_Articles_Word2Vec.ipynb

Word count from all the articles is as shown below. <br>
<br>
![demo](https://github.com/Jun-Tam/article_analysis_word2vec/raw/master/images/word_count.png)
<br>
 
Word Cloud is a usefull tool to visualize what were people's interests in each year. <br>
<br>
![demo](https://github.com/Jun-Tam/article_analysis_word2vec/raw/master/images/word_cloud.png)
<br>
 
Using word2vec "ness" vectors are defined, and each article is converted into ness vectors. <br>
The time-series plots below show recent article trends for individual ness vectors along with oil price history. <br>
<br>
![demo](https://github.com/Jun-Tam/article_analysis_word2vec/raw/master/images/article_trend.png)
<br>

### Reference
Natural Language Processing In Action, Undestanding, analyzing, and generating text with Python, Manning <br>
Hobson Lane, Cole Howard, Hannes Max Hapke <br>
