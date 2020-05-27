# ELab-Report-Downloader-SRM
Automation of Downloading ELAB using Selenium

Ensure You have pip installed the things in requirements.txt

You can use pip install -r Requirement.txt

The Program requires the following inputs:

Username => Your register id which you use as a Username

Password => Your Passowrd with which you login(Don't worry it is just used to access the portal, you can check the code)

Login Page URL => The Login Page URL of the ELab you are going to download the reports from.

Course No => The number of blue block in the home page for your course(USED IF THERE ARE MULTIPLE COURSES IN SINGLE LAB)(If only one enter as one)

Level Url => The Q1 URL of the Level you are going to download from

The Files are downloaded in the Downloads Folder of Your Desktop

In case of any Question Report not being generated, the failure question number will be put in a text file called "Failed to download.txt"
