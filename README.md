[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/_PlaFtPA)
# Instructions

This final project involves working in groups of 3 to 5 members on a web app. The goal is to apply key software engineering practices discussed throughout the semester. You and your team will have the freedom to choose what to implement during this final project, as long as the requirements described below are met. 

# Requirements 

* The software must be a web app written in Python with the possibility of creating and authenticating users.
* Scrum must be used as the software development methodology. 
* The project must have a vision statement that describes the purpose of the software, the type of problem it aims to solve, and the target audience. 
* A use case diagram must be constructed to provide a high-level view of possible user interactions with the system. 
* You should describe at least six user stories in detail, including their acceptance criteria and point estimates.
* User stories must be referred to as US#1, US#2, etc. 
* At least one user story, not related to user creation or authentication, must be detailed using a sequence diagram.
* A class diagram should be built for the model classes used in the project, including their associations. 
* Create a GitHub repository for the project, following the file structure explained later in this document.
* Add all team members and the [instructor](https://github.com/thyagomota) as collaborators to the project’s GitHub repository.
* There should be two long-lived branches on this project: main (for the stable release) and dev (for the unstable release).
* The stable release is the one that is usually updated at the end of each sprint and includes the user stories that were considered done.
* The unstable release is the one that receives one or more updates during sprints.
* The main branch must be protected and require a code review before a pull request is approved.
* All source code must have a consistent header comment with a brief description and its author(s).
* Code written for this project must comply with the PEP8 code style standard.
* Code will be inspected for best practices related to commenting, naming, formatting, function decomposition, object-oriented programming (OOP), error handling, and more.
* At least one white-box and one black-box test, neither of them related to user creation or authentication, must be provided.
* A test coverage report must be generated using Python’s **coverage** tool.
* The final product must be deployed using Docker containerization technology.
* All requirements needed for the project must be frozen into a **requirements.txt** file.
* The project must have database persistence.
* A database other than SQLite must be used.
* At a minimum, a three-layer software architecture is expected for this project.
* The project should be deployed using Docker Compose (with at least two containers). 

# GitHub Repository Structure 

```
README.md
Dockerfile
docker-compose.yml
requirements.txt
src/
tests/
uml/
```
Use README_TEMPLATE.md for information about the format that you should use for the project's README file. 

Feel free to add other folders as you see fit.

# Project Submission

Commit this **README.md** file with the link of your project's GitHub repository below: 

```
GitHub repository: <  https://github.com/ahageman27/final-project-social-media-platform.git  >
```

# Rubric

+5 Project's README file: mission statement

+5 Project's README file: use case diagram

+5 Project's README file: sequence diagram 

+10 Project's README file: user stories (~ 6 x 1.5)

+5 Project's README file: class diagram for the model classes

+5 GitHub repository organization

+20 Project's README file: development process

+5 Code inspection: PEP8 compliance 

+5 Code inspection: comments, naming, functions, formatting, OOP best practices, error handling, etc.

+10 Code quality, including testing

+5 Project's README file: test coverage report using Python's **coverage**

+5 Project's Deployment

+15 team/self evaluation

Deductions: 

-10 user creation not available/working

-10 user authentication not available/working 

-5 for each user story not completed 

-5 **main** branch does not have consistent commits 

-5 **dev** branch does not have consistent commmits

-5 no burndown chart was created

# Overview

Use this section to outline the vision for the product to be developed, including a use case diagram that shows the main user interactions with the product, in order to provide readers with an overview of the project.

# Design

## User Stories

Describe the user stories designed for the project, including clear acceptance criteria and point estimate for each of them. User stories must be consistent with the use case diagram. Refer to the user stories using US#1, US#2, etc. At least one of the user stories, not related to user creation or authentication, must be detailed by a sequence diagram. 

US#1: User Registration

As someone outside of the platform, I want to register as a user so I can access posts on the social media platform. Given that the person is able to set up an account for the page, when the person signs up to the platform then they should be able to create posts and view the post of other Users

estimate of effort in terms of user story points: #5

US#2: User Posting

As a User, I want to be able to create a post so that my post will be seen by other users on the page. Given I have access to my homepage and am able to make a post, When I submit my post onto the page then my Post should be visible to other users and myself on the homepage

estimate of effort in terms of user story points: #5

US#3: User Deleting

As a User, I want to be able to delete a post so that my post will no longer be seen by other users on the page, Given I have access to my homepage and can find the post I wish to delete, when I hit delete on my post then my post should be removed from the homepage and database so it is no longer available.

estimate of effort in terms of user story points: #5

US#4: Administration Registration

As someone outside of the platform, I want to register as an administrator so I can monitor accounts and posts on the social media platform. Given that the person is able to set up an administration account for the page, when the person signs up to the platform they should be able to monitor Posts and Users.

estimate of effort in terms of user story points: #13

US#5: Administration Deleting Posts

As an Administrator, I want to be able to delete the posts of other Users on the platform. Given that a user created a post that breaks the rules on the page, when I hit delete on another Users post then that post should be removed from the homepage and database so it is no longer available.

estimate of effort in terms of user story points: #8

US#6: Administration Deleting Users

As an Administrator, I want to be able to delete the account of other Users on the platform. Given that a user's posts have shown to break the rules too much, When I hit delete on another Users account then that Account along with All posts in that account should be removed from the homepage and database so it is no longer available.

estimate of effort in terms of user story points: #8

## Sequence Diagram

At least one user story, not related to user creation or authentication, must be detailed using a sequence diagram.


## Model 

At a minimum, this section should have a class diagram that succinctly describes the model classes used in the project, including their associations.

# Development Process 

This section should be used to describe how the scrum methodology was used in this project. As a suggestion, include the following table to summarize how the sprints occurred during the development of this project.

|Sprint#|Goals|Start|End|Done|Observations|
|---|---|---|---|---|---|
|1|US#1, US#2, US#3, US#4 |04/23/24|05/02/24|US#1, US#2, US#3, US#4|...|
|2|US#5, US#6, Dockerfile, Testing & Submission |05/02/24|05/10/24|US#5, US#6, Dockerfile, Testing & Submission|...|

Use the observations column to report problems encountered during a sprint and/or to reflect on how the team has continuously improved its work. If you prefer, you can use the same format used in the project 2 (sprint markdown files). 

# Testing 

Share in this section the results of the tests performed to attest to the quality of the developed product, including the coverage of the tests in relation to the written code. There is no minimum code coverage expectation for your tests, other than expecting "some" coverage through at least one white-box and one black-box test.

|#|Tests|Start|End|Done|Observations|
|---|---|---|---|---|---|
|1|White-Box|05/08/24|05/10/24|x|no test running in 0.05s|
|2|Black-Box|05/08/24|05/10/24|x|no test running in 0.05s|
|3|Coverage Report|05/08/24|05/10/24|x|no test running in 0.05s, no coverage report obtained|

# Deployment 

The final product must demonstrate the integrity of at least 5 of the 6 planned user stories. The final product must be packaged in the form of a docker image. The project should be able to be deployed using: 

```
docker compose up
```
