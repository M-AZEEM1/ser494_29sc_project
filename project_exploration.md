What: identify the author(s) of the dataset(s), when the data set was constructed, how many
records it contains, the meanings of the fields/attributes, and compute an MD5 hash for each file.

(If a file was downloaded, provide the URL and the MD5 of that file. The MD5 hash of the
download and the one in your repo must match.)



#### SER494: Exploratory Data Munging and Visualization
#### Project: Detection of LLM-Synthesized Code 
#### Author: ???
#### Date: 3.4.2026


## Basic Questions
**Dataset Name:** AIGCodeSet
**Dataset Author(s):** Basak Gokce
**Dataset Construction Date:** 5.12.2025
**Dataset Record Count:** 15,166
**Dataset Field Meanings:** {Compiled from dataset description on https://huggingface.co/datasets/basakdemirok/AIGCodeSet}

|        Column        |                                          Description                                          |   |   |   |
|:--------------------:|:---------------------------------------------------------------------------------------------:|---|---|---|
| problem_id           |                                Unique problem ID from CodeNet.                                |   |   |   |
| submission_id        | Submission ID from CodeNet. "submission_id == unrelated" indicates purely LLM-generated code. |   |   |   |
| (12 CodeNet columns) |                        Metadata columns directly provided by CodeNet.                         |   |   |   |
| LLM                  |                          "Human", "CODESTRAL", "GEMINI", or "LLAMA".                          |   |   |   |
| status_in_folder     |                      Submission status: "wrong", "runtime", "accepted".                       |   |   |   |
| code                 |                  The code, which will either be LLM-written or human-written                  |   |   |   |
| label                |                       0 for Human-written code, 1 for LLM-written code                        |   |   |   |
| ada_embedding        |                              Ada embedding vectors of the code.                               |   |   |   |
| lines                |                                    Total number of lines.                                     |   |   |   |
| code_lines           |                                Number of non-empty code lines.                                |   |   |   |
| comments             |                                   Number of comment lines.                                    |   |   |   |
| functions            |                               Number of functions in the code.                                |   |   |   |
| blank_lines          |                                    Number of blank lines.                                     |   |   |   |


**Dataset File Hash(es):**  (Note: Updated 5/2 for workflow submission; fixed MD5)
Dataset 1 URL - AIGC samples: https://huggingface.co/datasets/basakdemirok/AIGCodeSet/blob/main/data/created_dataset_with_llms.csv
Dataset 1 MD5 Hash: fa826d77880bb6cb10f4e52d1e5df9f3

Dataset 2 URL - Human samples: https://huggingface.co/datasets/basakdemirok/AIGCodeSet/blob/main/data/human_selected_dataset.csv
Dataset 2 MD5 Hash: 2e39013dc63ec7107a2bd05c2223e8e6

## Interpretable Records
### Record 1 - from AIGC SAMPLES DATASET 
**Raw Data:** 

[p03243, s556163757, GEMINI, Runtime, 
"`N = int(input())
if N % 111 == 0:
  print(N)
else:
  for i in range(10):
    if N // 111 == i:
      print(111 * (i + 1))`", 1]

Interpretation:** 
IBM CodeNet is a dataset with samples of code solutions to coding problems. In the row of data above, the first number is the unique ID number for the 
problem that this code sample is for. The second number (submission ID) is similarly another unique identifier but that is linked to this specific submission where the sample is from, akin to how Gradescope
has different submissions. The third field simply states that Gemini was the LLM used to generate the code sample. The fourth field, 'Runtime', essentially states that the submission had a runtime error as its status.
The exact code sample is under the 5th field, and the 6th and final field has a label of 1 which is a flag to tell us the code is LLM generated.

From this interpretation, nothing is for sure unreasonable for this data row.

### Record 2 - from HUMAN SAMPLES DATASET
**Raw Data:** 

[s242112093, p03166, u575045134, 1589850395, Python, PyPy3 (2.4.0), py, Accepted, 1280.0, 182272.0, 518, , Accepted,
"`import sys
sys.setrecursionlimit(1000000)
def dfs(u):
    if(dp[u]!=-1):
        return dp[u]
    for i in d[u]:
        if(dp[i]!=-1):
            dp[u]=max(dp[u],dp[i]+1)
        else:
            dp[u]=max(dp[u],dfs(i)+1)
    return max(dp[u],0)
from collections import defaultdict as dd
n,m=map(int,input().split())
d=dd(list)
for i in range(m):
    u,v=map(int,input().split())
    d[u].append(v)
dp=dd(lambda: -1)
mx=0
for i in range(1,n+1):
    if(dp[i]==-1):
        dp[i]=dfs(i)
    mx=max(mx,dp[i])
print(mx)`", 0, Human]

**Interpretation:**
This data row is from the human code samples dataset. We learn here that we're looking at a code sample for the problem
with ID p03166, from the submission with id s242112093. The user who wrote the code has id of u575045134. The next 
handful of columns tell us that the code was written in Python (specifically PyPy3 version 2.4.0) and was saved with 
a .py extension. The code was accepted as a correct solution. The actual code itself was 518 characters long and was 
written by a human. I searched and was not yet able to find how to interpret '1589850395' from the date field, so this
is something I will have to be on the lookout for in the future. Regarding the remaining data, we know the submission
took 1280 seconds to run on the CPU and 182272 KB of memory. Lastly, the code itself seems to be a recursive depth-first search
algorithm.

Now with regard to sanity checking this data, the only value that I initially thought might not make sense was the memory value. 
Here in the IBM CodeNet repo README (https://github.com/IBM/Project_CodeNet/tree/main?tab=readme-ov-file#example-of-getting-the-metadata-for-a-particular-source-file)
it states that the memory used field in the metadata is measured in kilobytes. However, 182272 KB = 180 MB and this is significantly more memory
than several other submissions in the dataset. So comparing to a typical code
submission this may seem wildly out of range, but given this is a recursive DFS algorithm, after further research I realized that this
probably makes sense given potential complexity of the code sample. Therefore, I conclude that so far, nothing is deemed unreasonable
for sure from this data row.


## 'Human Selected Dataset' Features for Computing Statistics ##

Qualitative: 'status', 'problem_id' 
NOTE: id can help us track different attempts at answering the same problem and compare their code for takeaways

Quantitative: 'code_size', 'memory', 'cpu_time'


## Background Domain Knowledge (~310 words)
As is well-known, one of the popular uses for LLM’s and generative AI is for generating code. On the
surface level the difference in output between LLM code and human-written code may not seem apparent, 
since the former was trained on the latter, but there are various methods and clues that help one deduce
whether a code sample was authored by man or machine and that is the eventual end goal of this project.
For instance, AI-generated code tends to be more repetitive and in some areas longer, such as when it 
comes to function name length (https://arxiv.org/abs/2508.21634). Upon closer examination, it may 
become apparent that such code produced by LLM’s tends to be very verbose and even at times 
unnecessarily descriptive. This phenomenon has also been found when it comes to program comments, 
where even a simple function, for instance an ‘add(x1, x2)’ method that literally just returns x1 + x2, 
may have documentation explicitly stating ‘This method returns the sum of two numbers’ which any 
ordinary programmer may never explain to this degree. Beyond just names, AI generated code concerning 
logic can be significantly longer as well due to irrelevant package imports, impractical structure 
choices, and repetitiveness (Why AI-Generated Code Costs More to Maintain Than Human-Written Code). 
Interestingly enough, other breadcrumbs can also give us a hint on the authorship of a code sample, 
such as traces from StackOverflow posts merged together, cyclomatic complexity metrics, and even 
comment-to-code ratios (Was this Python written by a human or an AI? 7 signs to spot LLM-generated 
code - DEV Community). On top of this, performance-wise it was found that AI-generated code 
demonstrated 1.42x more performance issues as compared to human-written code, which shows us the 
overhead from  employing the usage of AI coding tools (AI-authored code needs more attention, 
contains worse bugs • The Register). 

source links: 
- https://dev.to/dev_tips/was-this-python-written-by-a-human-or-an-ai-7-signs-to-spot-llm-generated-code-3370
- https://www.altersquare.io/ai-generated-code-maintenance-costs/#:~:text=Key%20Differences%20in%20Performance%20Metrics&text=This%20comparison%20underscores%20the%20trade,demands%20of%20long%2Dterm%20growth.
- https://arxiv.org/abs/2508.21634



## Dataset Generality
The samples I am using for in my chosen dataset is actually from a relevant real-world project in the
same project domain. My data is sourced from IBM CodeNet, which is a large repository for code samples
written by both AI and humans. The structure seems to be a bit like leetcode where problems 
are submitted answers for, and these answers are then 'graded'. There is already literature existing
on similar subject matter for CodeNet so I trust this is a tried-and-true source of information. Additionally,
code is typically written to solve problems and just like how Leetcode is used by interviewers to gauge applicants,
this level of data allows me to compare the performance of humans vs LLM's for the same coding problem
and gauge the differences in style, performance, other metrics, etc.

## Data Transformations
### Transformation N
**Description:** 
No transformation were applied. I was able to do what I have done so far by using the 
downloaded csv files from CodeNet and leveraging library functions and/or strip out parts of data in-place.

## Visualizations (Note: updated 5/2 with missing analyses)

### Visual 1 - AB.png
**Analysis:**
This visual demonstrated a bit of a surprising correlation that I did not expect. Here it is apparent that the shortest 
code samples have a pattern of taking the longest time on the CPU. I typically would have expected the opposite!

### Visual 2 - AC.png
**Analysis:**
This visual revealed that, interestingly enough, the shortest code samples tended to take the most memory. 
Again, this was also a bit of a surprising correlation as I did not expect this. I am postulating that this 
could be in part due to less efficient code, but this may require deeper investigation into the samples themselves.

### Visual 3 - BC.png
**Analysis:**
This visual compared memory usage against CPU time, and depicted that the vast majority of
code submissions in the dataset were low in memory usage but low-to-mid in CPU time. The scatterplot 
showed that code samples exhibited a greater spread in terms of CPU times as opposed to memory usage which 
stayed relatively low as aforementioned.

### Visual 4 - prob_id_histogram.png
**Analysis:**
The histogram here illustrated that problem id's between 2600 and 3000 had the highest comparative number
of submissions. Interestingly, the number of samples we have for problem id's above 3000 generally
decreases with some very sharp spikes here and there. The problem id's with the most attempted
submissions seem to between 2700-2900.

### Visual 5 - status_histogram.png
**Analysis:**
This histogram depicted something that I don't know if I would've known about otherwise, and that is
the fact that the dataset has equivalent submissions of each status type. I'm assuming
this was done intentionally for variation in the dataset when CodeNet was being compiled, because
Accepted status submissions number the same as Runtime Error submissions and also Wrong Answer submissions.
This was personally an interesting find for me that was much easier to recognize graphically.