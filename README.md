# LOG ANALYSIS

## What is it?
 Python program that connects to a postgresql database containing logs and analyses the logs.

## Installation steps
 Please follow the steps below:

### Pre-requisites:
 * Python 2.7 - https://www.python.org/downloads/
 * Any text editor for editing the code(Sublime text preferred - https://www.sublimetext.com/download)
 * [Vagrant](https://www.vagrantup.com/)
 * [Virtual box - v4.3 preferred](https://www.virtualbox.org/)
 * [Git](https://git-scm.com/downloads)

### Steps
 1. Clone [Udacity Full Stack Nano Degree VM Repository](https://github.com/udacity/fullstack-nanodegree-vm)
 2. Launch [Vagrant VM](https://www.vagrantup.com/docs/)
    * Run 'vagrant up' command in the 'Udacity Full Stack Nano Degree VM Repository' clone folder
     (It may take a while to complete if you have never run it before)
    * Run 'vagrant ssh' command
 3. Create new folder at /vagrant/log_analysis/
 4. Clone/Fork this repository in log_analysis folder
 5. Extract 'newsdata.zip' in the same folder
 6. Run 'psql -d news -f newsdata.sql' command on vagrant ssh to import news data
 7. Run 'psql news -f sql_def.sql' command to create views from sql_def file
 8. Make changes to sql_def.sql file if required ([sql_def.sql](https://github.com/ahmfrz/Log_Analysis/blob/master/sql_def.sql))
 9. Make changes to Python functions ([log_analysis_report.py](https://github.com/ahmfrz/Log_Analysis/blob/master/log_analysis_report.py))
 10. Run command 'python log_analysis_report.py'

### Output
----------------------------------------------------------------
What are the most popular three articles of all time?
"Candidate is jerk, alleges rival"--338647 views
"Bears love berries, alleges bear"--253801 views
"Bad things gone, say good people"--170098 views


Who are the most popular article authors of all time?
Ursula La Multa--507594 views
Rudolf von Treppenwitz--423457 views
Anonymous Contributor--170098 views
Markoff Chaney--84557 views


On which days did more than 1% of requests lead to errors?
July, 17 2016--2.26% errors
----------------------------------------------------------------

## How to Contribute

Find any bugs? Have suggestions? Contributions are welcome!

First, fork this repository.

![Fork Icon](fork-icon.png)

Next, clone this repository to your desktop to make changes.

```sh
$ git clone {YOUR_REPOSITORY_CLONE_URL}
$ cd folder
```

Once you've pushed changes to your local repository, you can issue a pull request by clicking on the green pull request icon.

![Pull Request Icon](pull-request-icon.png)

## License

The contents of this repository are covered under the [MIT License](LICENSE).
