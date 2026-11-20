CREATE TABLE students (student_id INTEGER PRIMARY KEY, full_name VARCHAR(100) NOT NULL, city VARCHAR(80), joined_on DATE NOT NULL);
CREATE TABLE courses (course_id INTEGER PRIMARY KEY, course_name VARCHAR(100) NOT NULL UNIQUE, monthly_fee DECIMAL(10,2) NOT NULL CHECK (monthly_fee >= 0));
CREATE TABLE enrollments (enrollment_id INTEGER PRIMARY KEY, student_id INTEGER NOT NULL REFERENCES students(student_id), course_id INTEGER NOT NULL REFERENCES courses(course_id), enrolled_on DATE NOT NULL, status VARCHAR(20) NOT NULL DEFAULT 'active' CHECK (status IN ('active','paused','completed')));
