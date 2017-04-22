# In your face: The biased judgment of fear-anger expressions in violent offenders.

Martin Wegrzyn, Sina Westphal & Johanna Kissler,
in preparation

### Abstract

Why is it that certain violent criminals repeatedly find themselves engaged in brawls? Many inmates report having felt provoked or threatened by their victims, which might be due to a tendency to ascribe malicious intentions when faced with ambiguous social signals, termed hostile attribution bias.
The present study presented morphed fear-anger faces to prison inmates with a history of violent crimes, a history of child sexual abuse, and to matched controls form the general population. Participants performed a fear-anger decision task. Analyses compared both response frequencies and measures derived from psychophysical functions fitted to the data. In addition, a test to distinguish basic facial expressions and questionnaires for aggression, psychopathy and personality disorders were administered.
Violent offenders present with a reliable hostile attribution bias, in that they rate ambiguous fear-anger expressions as more angry, compared to both the control population and perpetrators of child sexual abuse. Psychometric functions show a lowered threshold to detect anger in violent offenders compared to the general population. This effect is especially pronounced for male faces, correlates with self-reported aggression  and presents in absence of a general emotion recognition impairment.
The results indicate that a hostile attribution, related to individual level of aggression and pronounced for male faces might be one mechanism mediating physical violence.

### About

This is a repository containing the full data and code of our paper about facial expression recognition in violence offenders.

### Table of Contents

- the participant data
  - [AFAS](experiment/quest/app/static/logfiles)
  - [PPI-R](experiment/ppi_r.csv)
  - [SCID-II](experiment/scid_ii.csv)
  - [basic expressions and morphed expressions](experiment/data)
- the experiment
  - [AFAS as online questionnaire](experiment/quest)
  - [face recognition experiment](experiment/emoFaces.py)
- the code
  - [Analysis of Questionnaires](notebooks/001_questionnaires.ipynb)
  - [Analysis of basic expressions recognition](notebooks/002_basicExpressions.iypnb)
  - [Importing morph data](notebooks/003_gettingMorphData.iypnb)
  - [Basic analyses of morph data](notebooks/004_basicPlotting.ipynb)
  - [Curve Fitting/Psychophysics](notebooks/005_fittingFunctions.ipynb)

### Requirements

Data analysis was performed with Python 2.7 [www.python.org](http://www.python.org) using mainly numpy, scipy, pandas, scikit-learn, matplotlib, seaborn and jupyter.



To run all the scipts, you can create a virtual environment, by first installing virtualenv


```shell
pip install  virtualenv
```
Then you can create a virtual environment in the folder into which you cloned this repository

```shell
virtualenv venv
```

and then install all modules using pip


```shell
venv/bin/pip install -r requirements.txt
```

The main experiment was written and rendered with [PsychoPy](http://psychopy.org).
The AFAS questionnaire was rendered as a html site using [Flask](http://flask.pocoo.org/) for the back-end.

### Contact

For questions or comments please write to [martin.wegrzyn@uni-bielefeld.de](mailto:martin.wegrzyn@uni-bielefeld.de)
