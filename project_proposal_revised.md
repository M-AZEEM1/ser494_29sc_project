#### SER494: Project Proposal
#### Detection of LLM-Synthesized Code 
#### M-AZEEM
#### 3.23.2026
Keywords: AI-generated code, Deep learning, Vibe Coding


Description: 

The aim of this data science project is to determine how to identify AI Generated Code (AIGC). I plan to analyze a dataset/datasets of code samples from CodeNet of human and AIGC samples, and then cross reference the samples with each other to gain insights from a linguistic, syntactical, etc. point of view.
Some questions I would ask through this analysis are; What generally differs between the real and AIGC code? What patterns emerge? What structural code choices are made between humans and AI? Are there certain trends across the majority of the datasets in these regards?


Intellectual Merit: 

The discovery potential of my project is to help us gather the knowledge of how to identify the use of Generative AI in code. This research will hopefully go towards helping develop more specialized tools that can run on code samples to yield faster and more accurate results for verifying human code authenticity. 
This is an important field because the advent of Generative AI spawned an onslaught of problems with it being harder to prevent academic integrity violations, including specifically my subject area as well, software engineering. The 'quick and dirty' approach to vibe coding homework assignments has likely taken 
countless computer science students worldwide by storm and contributes to lack of integrity, in addition to output of university graduates with poorer quality of knowledge, skill, and competence, and essentially wounds said graduates' chances of thriving in the workforce. My research will hopefully contribute to battling
this issue by helping prevent the cheap approach to coursework and instead encouraging deep, intuitive understanding on course competencies.


Data Sourcing: 

My basic plan as of now is to go through CodeNet and sift through samples across
the two differing categories: human-generated samples, and LLM-generated samples. 
Each sample would have certain characteristics gathered from it, such as comment-to-function
ratio, cyclomatic complexity, etc. The choice for such features would be based on markers of
AIGC found from the latest research. The aim is to draw generalizations based on these
findings from the existence or lack thereof of certain markers within the samples, and
then continue onward to later train the data based on these findings. 

Background Knowledge:

1) Ramnarayanan, S. (n.d.). What is AI code generation? Benefits, risks, and tools. wiz.io. https://www.wiz.io/academy/ai-security/ai-code-generation 
2) Nihill, Caroline. “What to Do about Troubles with AI-Generated Code.” IT Brew, Morning Brew, 17 Mar. 2026, www.itbrew.com/stories/2026/03/17/troubles-with-ai-generated-code. Accessed 24 Mar. 2026.
3) “AI vs Human Code Gen Report: AI Code Creates 1.7x More Issues.” CodeRabbit, 2026, www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report.



Related Work:

1) devtips. “Was This Python Written by a Human or an AI? 7 Signs to Spot LLM-Generated Code.” DEV Community, 19 June 2025, dev.to/dev_tips/was-this-python-written-by-a-human-or-an-ai-7-signs-to-spot-llm-generated-code-3370. Accessed 24 Mar. 2026.
2) Motiwala, Huzefa. “Why AI-Generated Code Costs More to Maintain than Human-Written Code.” AlterSquare, 5 Nov. 2025, www.altersquare.io/ai-generated-code-maintenance-costs/. Accessed 24 Mar. 2026.
3) Cotroneo, Domenico, et al. “Human-Written vs. AI-Generated Code: A Large-Scale Study of Defects, Vulnerabilities, and Complexity.” ArXiv.org, 2025, arxiv.org/abs/2508.21634.
4) Esteban Cuellar Argotty, Juan, and Ruben Manrique. “AI-Generated Code Detection: An Examination of Current Tools in Education.” Generative Systems and Intelligent Tutoring Systems, edited by Sabine Graf and Angelos Markos, vol. 15723, Springer Nature Switzerland, 2026, pp. 192–201, https://doi.org/10.1007/978-3-031-98281-1_15.
5) Pan, Wei Hung, et al. “Assessing AI Detectors in Identifying AI-Generated Code: Implications for Education.” IEEE/ACM International Conference on Software Engineering: Software Engineering Education and Training (Online) [New York, NY, USA], 2024, pp. 1–11, https://doi.org/10.1145/3639474.3640068.
6) Zhang, Zixian, and Takfarinas Saber. “Exploring the Boundaries Between LLM Code Clone Detection and Code Similarity Assessment on Human and AI-Generated Code.” Big Data and Cognitive Computing [BASEL], vol. 9, no. 2, no. 41, February 2025, https://doi.org/10.3390/bdcc9020041.



Questions:

1) RO1 - Describe the unique trends of differing characteristics between AIGC vs. Human-written code.
2) RO2 - To predict the value of the likelihood of a certain code sample being AIGC based on a list of factors/markers such as comment-to-function ratio, overdocumentation, etc.
3) RO3 - To defend the model for performing the prediction of likelihood of a code sample being AIGC
4) RO4 - To evaluate causal relationships implied by the RO2 model



Preregistration:

Potential input features:
- A - cyclomatic complexity
- B - comment-to-function ratio
- C - code size

Target feature: percent likelihood of the sample being AIGC

To answer bullet point 3, I expect the three potential input features above may already have the most significant 
impact on prediction (when considering existing features)


Feature 1 Hypothesis:
I hypothesize that a higher cyclomatic complexity score may lead to a higher chance of the model
classifying the code being written by AI, as evidenced by research (such as here: https://vfast.org/journals/index.php/VTCS/article/view/2043/1695)

Feature 2 Hypothesis:
Likewise, I hypothesize that a high comment-to-function ratio (high determined by exceeding a set threshold
based on research findings) will cause the model to increase its chance of assigning a higher likelihood
percentage of being AIGC

Feature 3 Hypothesis:
Lastly, I hypothesize that larger code size may slightly boost the model's prediction percentage of
AIGC since Generative AI tends to be more unnecessarily verbose when writing code.


I think that there may be a positive or non-inverse correlation between AB, BC, and AC since each 
feature serves to boost model prediction rates for AIGC due to the existence of the feature,
I expect that BC may have the strongest correlation since C somewhat depends on B - code size
will go up if there are more comments in the code, and both of these may indicate a stronger likelihood
of the code being AIGC.
