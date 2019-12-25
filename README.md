# Article Analysis by word2vec and Principal Component Analysis (PCA)

### Summary
This Jupyter Notebook demonstrates application example of NLP to news articles in PDF. <br>

More than 700 articles related to energy industry were collected and converted into text files. <br>
Word count from all the articles is as shown below. <br>
![demo](https://github.com/Jun-Tam/article_analysis_word2vec/raw/master/images/word_count.png)

As a word vector in word2vec has 300 dimensions, dimension reduction is necessary to ease interpretation of the result. <br>
PCA is used for dimension reduciton, and here's the scree plot obtained by fitting yearly averaged word vectors. <br>
![demo](https://github.com/Jun-Tam/article_analysis_word2vec/raw/master/images/pca_screeplot.png)

As a next step, 7 "ness" vectors were defined to interpret each principal component (PC). <br>
1st PC shows high eigenvalue for "environmentness", for example. <br>
![demo](https://github.com/Jun-Tam/article_analysis_word2vec/raw/master/images/pc_vs_ness-vector.png)

These figures show PC1 and PC2 for yearly averaged article vectors (right) and frequent words in all the articles (left). <br>
It can be inferred that environmental topic is getting more attention year by year. <br>
![demo](https://github.com/Jun-Tam/article_analysis_word2vec/raw/master/images/pc_vs_ness-vector.png)

Word Cloud is a usefull tool to visualize what were people's interests in each year.
![demo](https://github.com/Jun-Tam/article_analysis_word2vec/raw/master/images/word_cloud.png)


### Reference
Natural Language Processing In Action, Undestanding, analyzing, and generating text with Python, Manning <br>
Hobson Lane, Cole Howard, Hannes Max Hapke <br>
