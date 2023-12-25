# Recommender System for HUSTer Extracurricular Engagement

## Introduction 

Activity scores are becoming crucial for HUST students, impacting their degrees and credit limits. Students can earn activity scores by participating events presented at ctsv.hust.edu.vn. Our project uses data from the CTSV website to develop a recommender system, answering questions for managers: "Which types of activities are students likely to attend?" and for students: "Which activities should I attend?"

To address this problem, we first cleaned and conducted exploratory data analysis on the data collected from the CTSV API. After performing intensive and extensive analysis on the dataset, we formalized the problem as implicit recommendation and implemented several types of approaches to build our recommender system, including collaborative filtering, content-based, and hybrid methods.

## Environment Setup
```
pip install requirements.txt
```

## Running the project 

1. Download the [`output.zip`](https://drive.google.com/file/d/1xyrCCzVaHxj6E_v2Hm3cMNOXi-fomzit/view?usp=sharing) and unzip them to notebooks/ or you need to crawl the data again
2. You can choose the notebooks you want to run from 1 to 8
3. For NCF model, please follow the `README.md` in `NCF/` folder 