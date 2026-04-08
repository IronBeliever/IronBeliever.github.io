---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

👋🏻Hi, I'm Ge Yuan. I'm a second year Ph.D student from the [Department of Computer Science and Technology](http://www.cse.neu.edu.cn) at [Northeastern University, China](https://www.neu.edu.cn). I work at [Natural Language Processing Lab](http://team.neu.edu.cn/NEUNLPLab/zh_CN/index.htm) under the supervision of Prof. [Tong Xiao](https://www.nlplab.com/members/xiaotong) and Prof. [Jingbo Zhu](https://www.nlplab.com/members/zhujingbo.html).

My research interest includes speech language process, multi-reward RL, and continue language modeling. I have published more than 10 papers at the top international AI conferences with total <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'>google scholar citations <strong><span id='total_cit'>70+</span></strong></a> (You can also use google scholar badge <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>).


# 🥳 News
- *2026.04*: Open to new opportunities: Seeking an internship👋🏻.
- *2026.04*: &nbsp;🎉 Two papers (1 **_Top 5% of accepted papers_** by Main Conference and 1 Fingdings) accepted by [ACL 2026](https://2026.aclweb.org).
- *2026.02*: &nbsp;🎉 Four papers accepted by [ICASSP 2026](https://2026.ieeeicassp.org).
- *2025.11*: &nbsp;🎉 Two papers accepted by [AAAI 2026](https://aaai.org/conference/aaai/aaai-26/).
- *2025.08*: &nbsp;🎉 One paper (Main Conference) accepted by [EMNLP 2025](https://2025.emnlp.org).
- *2025.06*: &nbsp;🎉 One paper (Oral) accepted by [NLPCC 2025](http://tcci.ccf.org.cn/conference/2025/).
- *2026.02*: &nbsp;🎉 One paper accepted by [ICASSP 2025](https://2025.ieeeicassp.org).
- *2024.08*: &nbsp;🎉 One paper (Main Conference) accepted by [EMNLP 2024](https://2024.emnlp.org).
- *2024.06*: Finished my internship at Huawei.
- *2024.02*: &nbsp;🎉 One paper accepted by [LREC-COLING 2024](https://lrec-coling-2024.org).
- *2023.06*: Started my internship at Huawei.


# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2024</div><img src='images/car.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Clustering and ranking: Diversity-preserved instruction selection through expert-aligned quality estimation](https://aclanthology.org/2024.emnlp-main.28.pdf)

**Yuan Ge**, Yilun Liu, Chi Hu, Weibin Meng, Shimin Tao, Xiaofeng Zhao, Hongxia Ma, Li Zhang, Boxing Chen, Hao Yang, Bei Li, Tong Xiao, Jingbo Zhu

Cited by _Google DeepMind_, _Meta GenAI_, _Baichuan Technical Report_, _CMU_, and other organizations; \\
Email Invitation for Internships at _Tongyi Lab_; \\
Introduced in _Liu Cong’s NLP_ WeChat Official Account(刘聪NLP); \\
Introduced in the _YSSNLP 2024 Tutorial_;

[**Project**](https://github.com/IronBeliever/CaR) <strong><span class='show_paper_citations' data='7_4WS_kAAAAJ:d1gkVwhDpl0C'></span></strong>
- We discuss the importance of **data quality** and **data governance**, and design a data filtering method that takes both **data quality and diversity** into account. Our method achieves open-ended dialogue performance that is 32.1% better than the baseline using the full dataset on the Alpaca dataset, while utilizing only **_1.96%_** of the data. More importantly, we demonstrate that _the benefits of data governance during the SFT stage remains significant_ even as the number of _parameters of the pre-trained model increases (7B–30B)_ and the _model’s pre-training capabilities improve (Llama 1–Llama 3)_. As of 2023, there is still no consensus on the impact of data quality on advanced LLMs.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2026</div><img src='images/speech_gap.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[On the Emotion Understanding of Synthesized Speech](https://arxiv.org/pdf/2603.16483)

**Yuan Ge**, Haishu Zhao, Aokai Hao, Junxiang Zhang, Bei Li, Xiaoqian Liu, Chenglong Wang, Jianjin Wang, Bingsen Zhou, Bingyu Liu, Jingbo Zhu, Zhengtao Yu, Tong Xiao

**SAC rating: 10**: **_Top 5%_** of accepted papers, seminal paper. Recommended for an _oral presentation_. \\
Average Overall Assessment: **4.00** (Min: 3.5, Max: **4.5**); Meta: 3.5

[**Project**](https://github.com/965002973/Synthesis_SER) 
- Synthetic audio is becoming increasingly common, yet audio understanding tasks have largely overlooked it. It is widely believed that _emotion understanding models learn fundamental representations that transfer to synthesized speech_, making emotion understanding results _a plausible reward or evaluation metric_ for assessing emotional expressiveness in speech synthesis. In this work, we find that **current SER models can not generalize to synthesized speech**, largely because **speech token prediction during synthesis induces a representation mismatch** between synthesized and human speech. Moreover, generative Speech Language Models (SLMs) tend to _infer emotion from textual semantics while ignoring paralinguistic cues_. Overall, our findings suggest that **existing SER models often exploit non-robust shortcuts rather than capturing fundamental features**, and paralinguistic understanding in SLMs remains challenging.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2026</div><img src='images/sagelm.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SageLM: A Multi-aspect and Explainable Large Language Model for Speech Judgement](https://ojs.aaai.org/index.php/AAAI/article/view/40338)

**Yuan Ge**, Junxiang Zhang, Xiaoqian Liu, Bei Li, Xiangnan Ma, Chenglong Wang, Kaiyang Ye, Yangfan Du, Linfeng Zhang, Yuxin Huang, Tong Xiao, Zhengtao Yu, JingBo Zhu

[**Project**](https://github.com/IronBeliever/SageLM)
- Current evaluations of Speech-to-Speech (S2S) models rely on _human evaluation_ or _“ASR + text evaluation.”_ This approach 1. suffers from _cascading errors_; 2. _ignores the paralinguistic information_ inherent in spoken dialogue. Therefore, we constructed **a dataset** and trained **a multidimensional, end-to-end, interpretable speech evaluation model**. We found that _using results plus explanations for SFT within the LLM-as-a-judge paradigm yields better performance than GRPO_. Furthermore, we comprehensively tested SageLM’s evaluation capabilities and preliminarily validated its performance as a reward model.
</div>
</div>

- **ICASSP 2026**, [MTP-S2UT: Enhancing Speech-to-Speech Translation Quality with Multi-token Prediction](https://arxiv.org/pdf/2510.10003?), Jianjin Wang, Runsong Zhao, Xiaoqian Liu, **Yuan Ge**, Ziqiang Xu, Tong Xiao, Shengxiang Gao, Zhengtao Yu, Jingbo Zhu
- **ICASSP 2026**, [StyleBench: Evaluating Speech Language Models on Conversational Speaking Style Control](https://arxiv.org/pdf/2603.07599), Haishu Zhao, Aokai Hao, **Yuan Ge**, Zhenqiang Hong, Tong Xiao, Jingbo Zhu
- **ICASSP 2026**, [Attention2Probability: Attention-Driven Terminology Probability Estimation for Robust Speech-to-Text System](https://arxiv.org/pdf/2508.18701), Yanfan Du, Jun Zhang, Bin Wang, Jin Qiu, Lu Huang, **Yuan Ge**, Xiaoqian Liu, Tong Xiao, Jingbo Zhu
- **ICASSP 2026**, [SUBQRAG: Sub-Question Driven Dynamic Graph RAG](https://arxiv.org/pdf/2510.07718), Jiaoyang Li, Junhao Ruan, Shengwei Tang, Saihan Chen, Kaiyan Chang, **Yuan Ge**, Tong Xiao, Jingbo Zhu
- **AAAI 2026**, [WaveEx: Accelerating Flow Matching-based Speech Generation via Wavelet-guided Extrapolation](https://ojs.aaai.org/index.php/AAAI/article/view/40490/44451), Xiaoqian Liu, Xiyan Gui, Zhengkun Ge, **Yuan Ge**, Chang Zou, Jiacheng Liu, Zhikang Niu, Qixi Zheng, Chen Xu, Xie Chen, Tong Xiao, Jingbo Zhu, Linfeng Zhang
- **EMNLP 2025**, [Step-level Verifier-guided Hybrid Test-Time Scaling for Large Language Models](https://aclanthology.org/2025.emnlp-main.931.pdf), Kaiyan Chang, Yonghao Shi, Chenglong Wang, Hang Zhou, Chi Hu, Xiaoqian Liu, Yingfeng Luo, **Yuan Ge**, Tong Xiao, Jingbo Zhu
- **NLPCC 2025**, [StoryBench: A Dataset for Diverse, Explainable, Multi-hop Narrative Text-to-Image Generation](https://idp.springer.com/authorize?response_type=cookie&client_id=springerlink&redirect_uri=https%3A%2F%2Flink.springer.com%2Fchapter%2F10.1007%2F978-981-95-3346-6_3), **Yuan Ge**, Kaiyang Ye, Saihan Chen, Aokai Hao, Xiangnan Ma, Kaiyan Chang, Tong Xiao, Jingbo Zhu
- **ICASSP 2025**, [A Modular-based Strategy for Mitigating Gradient Conflicts in Simultaneous Speech Translation](https://ieeexplore.ieee.org/abstract/document/10887794/), Xiaoqian Liu, Yangfan Du, Jianjin Wang, **Yuan Ge**, Chen Xu, Tong Xiao, Guocheng Chen, Jingbo Zhu
- **LREC-COLING 2024**, [RankPrompt: Step-by-Step Comparisons Make Language Models Better Reasoners](https://aclanthology.org/2024.lrec-main.1183.pdf), Chi Hu, **Yuan Ge**, Xiangnan Ma, Hang Cao, Qiang Li, Yonghua Yang, Tong Xiao, Jingbo Zhu


# 🎖 Honors and Awards
- *2024.10* Huawei Smart Base Scholarship(华为智能基座奖学金).
- *2022.06* Selected for the “Northeastern University–Huawei Digital and Networking Elite Class”(东北大学—华为数通菁英班) at the School of Future Technologies(未来技术学院). 

# 📖 Educations
- *2024.09 - 2026.04 (now)*, Ph.D, Northeastern University, under the supervision of Prof. [Tong Xiao](https://www.nlplab.com/members/xiaotong) and Prof. [Jingbo Zhu](https://www.nlplab.com/members/zhujingbo.html).
- *2022.09 - 2024.06*, Master, Northeastern University, under the supervision of Prof. [Tong Xiao](https://www.nlplab.com/members/xiaotong) and Prof. [Jingbo Zhu](https://www.nlplab.com/members/zhujingbo.html). 
- *2018.09 - 2022.06*, Undergraduate, Northeastern University. 

# 💻 Internships
- *2023.08 - 2024.08*, Research Intern & LLM Application Engineer, _Huawei_(Beijing, China).
