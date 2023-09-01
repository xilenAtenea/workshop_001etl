# Workshop_001etl - Python Data Engineer Workshop
Presented by Xilena Atenea Rojas Salazar 

## Welcome

Explore the Python Data Engineer Challenge – a practical simulation of a job interview experience.

The main purpose of this repository is to show a solution to a challenge that was created for the role of Python Data Engineer for a job interview.

The idea is to manipulate the data given to us in order to analyze it and create visualizations to demonstrate skills. The required visualizations are:

- Distribution of hires by technology (pie chart)
- Hires categorized by year (horizontal bar chart)
- Hires segmented by seniority (bar chart)
- Hires across years for select countries (USA, Brazil, Colombia, Ecuador) displayed through a multiline chart.

## Quick data overview

The CSV file contains the data of candidates who participated in a selection process for a job. It's important to note that this data is randomly generated. The task will be to perform extensive analysis and various data manipulations on this data set.

I have 50k rows of data about candidates. The fields I had were:

- First Name
- Last Name
- Email
- Country
- Application Date
- Yoe (years of experience)
- Seniority
- Technology
- Code Challenge Score
- Technical Interview

## Technologies Used

To make this exercise specific was used:

- python 3.10.5
- mysqlclient 2.2.0

This was done using VSC (Visual Studio Code). Other tools and modules were installed in a virtual environment to avoid compatibility issues, you will be able to install the requirements.txt to install them all instantly. We will see this in the Getting Started session.

## Repository overview

This repository is quite simple, so it only has the notebook “[etl_workshop.ipynb](https://github.com/xilenAtenea/workshop_001etl/blob/main/etl_workshop.ipynb)” that you have to run to get all the results, and the .gitignore that shows some used filenames that you probably have to create or get. These files will be discussed further in Considerations.

## Getting Started

In order to use this repository, you will need to

- Clone the repository, specifically using "git clone https://github.com/xilenAtenea/workshop_001etl"
- Create a virtual environment from your terminal. You can use: "python -m venv [environment_name]"
- Activate your virtual environment. You can use: "[environment_name]/scripts/activate"
- Install the required tools and modules in the environment. Use: "pip install -r requirements.txt".
- Set the created environment as kernel.
- Run all etl_workshop.ipynb and use it as needed.

## Considerations

- To establish the connection to the database, it´s necessary to have a file named "config_db.json" containing your database credentials in json format. This file should include the following key-value pairs: "localhost" for the server address, "user" for the username, "password" for the password, and "database" for the specific database you intend to access. Each key should be assigned its corresponding credential value.
- You should have a csv containing the data described in the Quick Data Overview session to obtain results very similar to those presented in this repository. However, you can use it only as a base or guide, so you could use another csv or other file containing the data you will use.
- If you are following the Getting Started instructions, don't forget to set the environment as kernel before you run the notebook.
