What: identify the author(s) of the dataset(s), when the data set was constructed, how many
records it contains, the meanings of the fields/attributes, and compute an MD5 hash for each file.

(If a file was downloaded, provide the URL and the MD5 of that file. The MD5 hash of the
download and the one in your repo must match.)



#### SER494: Exploratory Data Munging and Visualization
#### Project: Detecting Machine-Synthesized Code through Digital Forensics
#### Author: Mohammed Azeem
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


**Dataset File Hash(es):** TODO


## Interpretable Records
### Record 1
**Raw Data:** TODO
Interpretation:** TODO
### Record 2
**Raw Data:** TODO
**Interpretation:** TODO
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

