 
#### SER494: Machine Learning Evaluation
#### AIGC Code Detection Project
#### 4.20.26

## Evaluation Metrics
### Metric 1
**Name:** Precision

**Choice Justification:** Since my data science problem is a question of 
binary classification, precision is important because it shows the proximity
of our classification predictions to each other that help us gauge the factors
behind our model.


### Metric 2
**Name:** Accuracy

**Choice Justification:** This is a bit more simple to explain as the endgoal of 
the project is to correctly identify which code samples are AI-generated and which
ones are not. The accuracy metric allows us to grade our model and see whether it is
correctly making predictions above certain accuracy threshold. In the case that it is
not, we know to go back and fine-tune our model until no longer needed.

## Alternative Models
### Alternative 1: Polynomial regression
**Construction:** Based off my research, I ended up constructing this model by generating
polynomial features of degree 2, then creating a scikit-learn Linear Regression model,
then fitting that model to my polynomial features and my Y set.

**Evaluation:** Unfortunately, due to some issues in my data (which I spent I assume
the bulk of my hours on this assignment so far trying to fix, but to no avail), I was
not able to successfully run all my models. I tried to fulfill the 
parts of the assignment spec/rubric that didn't need running those models,
I do apologize for the shortcoming

### Alternative 2: LASSO
**Construction:** The LASSO regression model was constructed by first generating
a random regression problem and specifying the number of features, then creating a
linear model trained with L1 with alpha value set at 0.5 and my X set as a
parameter. The lasso model was then fit to a sample of data afterward.

**Evaluation:** Please see Evaluation 1!

### Alternative 3: ElasticNet
**Construction:** This model was constructed by first generating a regression problem
through the scikit-learn library method, set to two features and 0 random state. An
ElasticModel() was then created from that same library and then fit on 
my X and Y set.

**Evaluation:** Please see Evaluation 2!


**Best Model** (please see evaluation explanations above, sorry!)


## Visualization
### Visual N
**Analysis:** TODO

(duplicate above as many times as needed; remove this line when done)

## Best Model

**Model:** TODO
