-- Find most popular articles with author and number of views
CREATE VIEW most_popular AS
SELECT regexp_matches(replace(replace(lower(articles.title), E'\'', ''),
                              'there are a lot of', 'so many'), log_result.title),
articles.title, articles.author, views
FROM articles,
(SELECT replace(SUBSTRING(path FROM 10 FOR char_length(path)), '-', ' ')
 AS title, COUNT(*) AS views
 FROM log
 WHERE log.status='200 OK' AND char_length(path) > 2 GROUP BY title)
AS log_result ORDER BY views DESC;

-- Find all logs for each day
CREATE VIEW total_status AS
SELECT date_trunc('day', time) AS time_org, count(status)
FROM log
GROUP BY time_org;

-- Find all logs where status was not ok for each day
CREATE VIEW ng_status AS
SELECT date_trunc('day', time) AS time_org, count(status)
FROM log
WHERE status != '200 OK'
GROUP BY time_org;
