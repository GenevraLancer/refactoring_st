# Implementing architecture patterns by refactoring a python app
In this project I want to show a ways to refactor a python app. I will write about common use architectural patterns like DDD, CQSR and Clean Architecture.
Switch a branch to read about refactoring step you interested in.

## Buisness Requirements
In my company we have some projects in private git repositories. Each project is a set of folders, xml files and may contain other types of files.
The main task is to get information/statistics about objects placed inside of xml files. The second task is to modify xml files according to some business rules.

## Step 1. Create project structure
This is widely used presentation of clean architecture layers in an app. Some times the Services layer is called the Use case layer.

<img src="https://user-images.githubusercontent.com/25906422/178775519-78304cf5-3a8a-41e5-a571-3b12ff173b52.png" width="430" height="400">

The folder structure turned out like this. Main work an app do with the xml files in local git repository on the filesystem.
```
multitool   
│   
└───domain
│
└───infrastructure
│   │
│   └───adapters
│     │
│     └───filesystem
│   
└───services
```

## Step 2. Obtaining a service layer
I adore a [cosmic python book](https://www.cosmicpython.com/). I got from this book a first advice and start refactoring brunch 1_ball_of_mud from obtaining a service layer.


