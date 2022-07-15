# The Eudaimonia API
<div id="top"></div>
<span>
<img src="https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white" />
<img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
<img src="https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=Jira&logoColor=white">
<img src="https://img.shields.io/badge/Snyk-4C4A73?style=for-the-badge&logo=snyk&logoColor=white" />
<img src="https://img.shields.io/badge/Sentry-black?style=for-the-badge&logo=Sentry&logoColor=#362D59" />
<img src="https://img.shields.io/badge/Spotify-1ED760?&style=for-the-badge&logo=spotify&logoColor=white" />
</span>


## Table of Contents

- [Description](#description)
- [Frameworks and Tools](#frameworks-and-tools)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Roadmap](#roadmap)
- [Credits](#credits)


## Description

The Eudaimonia API is a semi-browsable suite of managed endpoints that helps the main Eudiamonia web application to work smoother by offloading large application code describing the NLP models for the mood analysis as well as the ML models for film recommendations.
<ul>
<li> API endpoints accessible with an API KEY that can be obtained upon submitting a request.</li>
<li> TMDB 5000 Movie Dataset from Kaggle used for the film recommendations. Logistic Regression algorithm for predictions. Additional inputs of mood for consideration is allowed.</li>
<li> Lexical-based NLP algorithms used for mood analysis. Textual input will get analysed and emotions such as Anger, Sadness, Happiness, Fear and Surprise would be evaluated.</li>
</ul>
The API was made with the intents of providing a solution for extensive sentiment analysis and recommending certain interests like books, movies, music, etc. that developers may use for their applications without having to reinvent the wheel.
The future scope of the project would be to extend its use-cases, provide schema and documentation and refining the models to make their performance optimal and better than the ones that are currently in the market that offer similar functionality but may not be clubbing all recommendation systems for use.

<p align="right">(<a href="#top">Top</a>)</p>


## Frameworks and Tools

The major frameworks, tools, services and APIs used for the making of this project is hereby listed:

* [Django REST](https://www.django-rest-framework.org): The API framework used to build the film and music recommendation system.
* [Postman](https://www.postman.com/): The API designing, testing and refinement tool used to make the API properly functional.
* [Scikit-Learn](https://scikit-learn.org/): Predictive model for movie recommendation.
* [Jira](https://www.atlassian.com/software/jira): The collaboration and software development tool used to simplify workflow.
* [Sentry](https://sentry.io/): The exception management service used for fatal error logging.
* [Snyk](https://snyk.io/): The security management service used for source code security vulnerability checks.
* [Spotify API](https://developer.spotify.com/documentation/web-api/quick-start/): API for music recommendation.
* [VSC](https://code.visualstudio.com/): The integrated IDE for development.

<p align="right">(<a href="#top">Top</a>)</p>


## Prerequisites

1. Install Python for your respective operating system at [https://www.python.org/downloads/](https://www.python.org/downloads/).

2. Install version control system of Git for your respective operating system at [https://git-scm.com/downloads](https://git-scm.com/downloads).

<p align="right">(<a href="#top">Top</a>)</p>


## Installation

1. Clone the repository:
    ```git
    git clone https://github.com/Diptonil/eudaimonia.git
    ```

2. Create a virtual environment for installation of required modules:
    ```py
    python -m venv venv
    venv\scripts\activate
    pip install -r requirements.txt
    ```

3. Run the website on the development server:
    ```py
    python manage.py runserver
    ```

Now the API is up and running (at port 8000 in case nothing else is mentioned). To access it, go to http://localhost:8000/.
Since the project is under developement, there is no frontend component to it as of now. It would be later added as the project edges towards production.

<b>IMPORTANT: Some files have not yet been committed and code is being refactored. The project is not functional as of now.</b>

The API shall soon be deployed and put to public use from which the endpoints would be directly accessible.

<p align="right">(<a href="#top">Top</a>)</p>


## Roadmap

There are subsequent upgrades to be made to the project to reach the final stage. Here are a list of all immediate objectives:

- [x] Configure initial particulars and services.
- [x] Develop authentication and authorization scheme.
- [ ] Service to request API key.
- [x] Develop mood analysis systems.
- [x] Develop film recommendation systems.
- [x] Develop music recommendation systems.
- [ ] Develop book recommendation systems.
- [ ] Configure the frontend of the system.
- [ ] Extend the prior features by refinement 
- [ ] Deploy using CI/CD practices.

<p align="right">(<a href="#top">Top</a>)</p>


## Achievements

- Third Place in the IEEE ComSoc Bangalore chapter hackathon 'CODIFY' arranged by BNMIT.

<p align="right">(<a href="#top">Top</a>)</p>


## Credits

The collaborators involved in this project are:

- Diptonil Roy

The academic and theoretical resources and articles utilized for this project are:
- [The Genre Theory in Film](https://www.cooperscoborn.org.uk/wp-content/uploads/2018/10/Genre-identify-all-of-the-theories-about-genre.pdf): A simplified and distilled version of the paper has been utilised, keeping in mind the nuances that any user may be capable of comprehending.
- [Ekman's Basic Emotion Model](https://www.paulekman.com/wp-content/uploads/2013/07/Basic-Emotions.pdf): The emotions considered for any particular user is of happiness, sadness, anger, fear and surprise.

<p align="right">(<a href="#top">Top</a>)</p>
