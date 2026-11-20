SELECT c.course_name, COUNT(*) AS active_students
FROM courses c JOIN enrollments e ON e.course_id = c.course_id
WHERE e.status = 'active'
GROUP BY c.course_name ORDER BY active_students DESC;

SELECT s.student_id, s.full_name, COUNT(*) AS course_count
FROM students s JOIN enrollments e ON e.student_id = s.student_id
GROUP BY s.student_id, s.full_name HAVING COUNT(*) > 1;

WITH totals AS (
 SELECT c.course_id, c.course_name, COUNT(e.enrollment_id) AS students
 FROM courses c LEFT JOIN enrollments e ON e.course_id = c.course_id AND e.status = 'active'
 GROUP BY c.course_id, c.course_name
)
SELECT course_name, students, DENSE_RANK() OVER (ORDER BY students DESC) AS popularity_rank FROM totals;
