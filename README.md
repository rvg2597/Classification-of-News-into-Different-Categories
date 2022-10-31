
# Classification of News into different categories

Lot of users visiting a news website are interested to read articles of specific category only. The news articles are categorised based on the content available in article, which allow readers to effortlessly read and find news of their preferred choice. The news is divided into different category by the author who writes the content of news article. Hence, author choose the best fit category for the article as they are requested by the newsfeed website to do. Classifying news into categories totally depends upon author’s opinion but this task becomes tedious when several news articles is to be published on news website simultaneously. This can increase the chance of error to classify news by the author due to load of work. Therefore, the process to tag news into particular category should be effectively automated since the terminology and vocabulary used by author in news article is indicative of particular category. The machine learning algorithms implemented were Naïve Bayes, Support Vector Machine, Decision tree, Random Forest and NLP algorithms like BERT implemented to achieve good accuracy.


## Data Collection

The dataset was collected using inshorts Indian news website (https://www.inshorts.com/en/read) of different categories such as technology, business, sports, politics, entertainment.

## Algorithms Implmented

1. Logistics Regression
2. Random Forest
3. Multinomial Naive Bayes
4. BERT
## Screenshots

First Page

[![first-page.png](https://i.postimg.cc/d32rW32g/first-page.png)](https://postimg.cc/jnjD2skh)

Implementation Page Using Random Forest

[![second-page.png](https://i.postimg.cc/3WMsjS83/second-page.png)](https://postimg.cc/gLDtmKL7)

Implementation using Logistics Regression

[![Third-Page.png](https://i.postimg.cc/50XvLpK7/Third-Page.png)](https://postimg.cc/MM8v80SV)
## Deployment

The project has been deployed on Heroku cloud.

https://classification-of-news.herokuapp.com/


## Conclusion

The algorithm which was implemented are Logistics Regression, Random Forest, Multinomial Naïve Bayes. The feature extractor which was implemented are Count Vectorizer, Term Frequency and Inverse Document Frequency (TF-IDF). The best model among these were Logistics Regression using Feature Extractor TF-IDF with accuracy of about 93% but due to some setbacks Bidirectional Encoder Representations from Transformers (BERT) was also implemented which gave almost the same accuracy. Since, BERT was able to solve the problems which Logistics Regression could not hence BERT can be considered as best performing model.