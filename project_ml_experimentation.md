#### SER494: Experimentation
#### AIGC Code Detection Project
#### 4.20.26


## Explainable Records
### Record 1
**Raw Data:** TODO

Prediction Explanation:** TODO

### Record 2
**Raw Data:** TODO

Prediction Explanation:** TODO

## Interesting Features
### Feature A
**Feature:** code_size

**Justification:** 
Within the problem domain, it has been found by research that AI-generated code samples
tend to feature more lines of code. This may be due to redundant/unnecessary imports,
over-commenting, etc. but it is a known trend. If a program is over the average program
length for a human in terms of LOC, it can be linked to a higher chance in being AIGC.

### Feature B
**Feature:** comment-to-function ratio


**Justification:** From my research, it was noted that AI tends to comment a lot and more robotically, even
for simple functions such as an addSum method that just adds two numbers together. Human 
coders do not typically comment this zealously if I am not mistaken, so a high c:f 
ration indicates higher potential for the sample to be AIGC.

### Feature B
**Feature:** cyclomatic complexity 

**Justification:** In this problem domain, cyclomatic compexity from AIGC may be less than humans by a significant margin
so this helps us point to another factor in detecting such generated code samples by analyzing
code structure.

## Experiments 
### Varying A
**Prediction Trend Seen:** TODO

### Varying B
**Prediction Trend Seen:** TODO

### Varying A and B together
**Prediction Trend Seen:** TODO


### Varying A and B inversely
**Prediction Trend Seen:** TODO

(duplicate above as many times as needed; remove this line when done)
