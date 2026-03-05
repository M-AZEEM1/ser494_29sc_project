What: identify the author(s) of the dataset(s), when the data set was constructed, how many
records it contains, the meanings of the fields/attributes, and compute an MD5 hash for each file.

(If a file was downloaded, provide the URL and the MD5 of that file. The MD5 hash of the
download and the one in your repo must match.)



#### SER494: Exploratory Data Munging and Visualization
#### Project: LLM-Synthesized Code Detection through Digital Forensics
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


**Dataset File Hash(es):** 
Dataset 1 URL - AIGC samples: https://huggingface.co/datasets/basakdemirok/AIGCodeSet/blob/main/data/created_dataset_with_llms.csv
Dataset 1 MD5 Hash: BE858EFDB3233DFF32B4CF239171DD686F9FB968D26CB0AB44C668FA40B2226E

Dataset 2 URL - Human samples: https://huggingface.co/datasets/basakdemirok/AIGCodeSet/blob/main/data/human_selected_dataset.csv
Dataset 2 MD5 Hash: F02F1099DE41434E67F26DD0470E8CCE32AC1A80966CEA51C8F9A25B95991DE8


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
Here in the IBM Codenet repo README (https://github.com/IBM/Project_CodeNet/tree/main?tab=readme-ov-file#example-of-getting-the-metadata-for-a-particular-source-file)
it states that the memory used field in the metadata is measured in kilobytes. However, 182272 KB = 180 MB and this is significantly more memory
than several other submissions in the dataset. So comparing to a typical code
submission this may seem wildly out of range, but given this is a recursive DFS algorithm, after further research I realized that this
probably makes sense given potential complexity of the code sample. Therefore, I conclude that so far, nothing is deemed unreasonable
for sure from this data row.





## Background Domain Knowledge
TODO
## Dataset Generality
TODO
## Data Transformations
### Transformation N
**Description:** TODO
**Soundness Justification:** TODO
(duplicate above as many times as needed; remove this line when done)
## Visualizations
### Visual N
**Analysis:** TODO
(duplicate above as many times as needed; remove this line when done)

