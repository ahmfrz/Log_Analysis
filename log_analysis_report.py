#!/usr/bin/env python2.7

import psycopg2

POPULAR_ARTICLES = '''
                    SELECT title, views
                    FROM most_popular
                    ORDER BY views DESC LIMIT 3;
                    '''

POPULAR_AUTHOR = '''
                SELECT authors.name, COUNT(most_popular.title),
                SUM(views) AS most_read
                FROM authors, most_popular
                WHERE authors.id = most_popular.author
                GROUP BY authors.name
                ORDER BY most_read DESC;
                '''

ERROR_STATUS = '''
                SELECT total_status.time_org as date, (
                round(
                (ng_status.count::numeric/total_status.count::numeric) * 100,2)
                )
                AS percent
                FROM total_status, ng_status
                WHERE total_status.time_org = ng_status.time_org
                AND ng_status.count > (total_status.count/100);
                '''


def db_connect(dbname='news'):
    """Connects to the PostgreSQL database and create cursor.
    Returns a database connection and cursor"""

    connection = psycopg2.connect("dbname=%s" % dbname)
    cursor = connection.cursor()
    return connection, cursor


def db_close(connection):
    """Closes the given connection"""

    connection.close()


def most_popular_articles():
    """Finds and prints the most popular articles of all time"""

    connection, cursor = db_connect()
    cursor.execute(POPULAR_ARTICLES)
    result = cursor.fetchall()
    db_close(connection)
    print "What are the most popular three articles of all time?"
    for item in result:
        print '"' + item[0] + '"--' + str(item[1]) + " views"
    print "\n"
    return result


def most_popular_author():
    """Finds and prints the most popular article author of all time"""

    connection, cursor = db_connect()
    cursor.execute(POPULAR_AUTHOR)
    result = cursor.fetchall()
    db_close(connection)
    print "Who are the most popular article authors of all time? "
    for item in result:
        print item[0] + '--' + str(item[2]) + " views"
    print "\n"
    return result


def error_status():
    """Finds and prints days where more than 1% of requests return error"""

    connection, cursor = db_connect()
    cursor.execute(ERROR_STATUS)
    result = cursor.fetchall()
    db_close(connection)
    print "On which days did more than 1% of requests lead to errors?"
    for item in result:
        print item[0].strftime("%B, %d %Y") + '--' + str(item[1]) + "% errors"
    return result

print "----------------------------------------------------------------"
most_popular_articles()
most_popular_author()
error_status()
print "----------------------------------------------------------------"
