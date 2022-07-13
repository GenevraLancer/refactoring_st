# Implementing architecture patterns by refactoring a python app
In this project I want to show a ways to refactor a python app. I will write about common use architectural patterns like DDD, CQSR and Clean Architecture.
Switch a branch to read about refactoring step you interested in.

## Buisness Requirements
In my company we have some projects in private git repositories. Each project is a set of folders, xml files and may contain other types of files.
The main task is to get information/statistics about objects placed inside of xml files. The second task is to modify xml files according to some business rules.

## Step 1. Start
On my mind, the simplest way to start parsing and modifying xml files is using the Jupiter Notebook. It has very friendly interface and you can use a google collab to develope the simplest app https://colab.research.google.com/notebooks/welcome.ipynb?hl=ru

## Step 2. Success
First version of an app was done. You can see it on this brunch.
I used a functional programming style here.
An app consist of two *.ipynb files. First file contain all function definitions and second file contain calls this functions.
A docker container was used to distribute the app inside the company.

## Step 3. Ball of mud
At the testing stage, it was discovered that some buisness projects has a different data sources structure [they used different types of xml files] 
And I had to modify functions definitions to meet new business requirements.
A small utility app became a large utility app. 

A large *.ipynb file looks like ball_of_mud programming style. It is not about functional programming anymore.
There is a point to make a sense about the app architecture.

Continue on the brunch 2_project_structure
