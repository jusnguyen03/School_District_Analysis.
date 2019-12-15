# School_District_Analysis.

## Project Overview
Maria, the Chief Data Scientist for a city school district, needs my help with analyzing a variety of data which includes student/school budgets and reading and math scores. These results show trends that will help her in discussions and strategic decisions at the school district level.

1. Calculate the total number students, total number of schools, total budget, average test scores, passing percentages.
2. Calculate the student count per school, budget per student, score averages per school, passing percentages per school.
3. Find the highest-performing schools and lowest-performing schools.
4. Establish spending ranges per student and per school.

## Resources
- Data Source: schools_complete.csv, students_complete.csv
- Software: Anaconda, Python 3.6.1, Jupyter Notebook, Visual Studio Code 1.38.1

## Summary
The analysis show that:
- There are 39,170 students vand 15 schools.
- The total school budget is $24,649,428
- The Average Scores per student and passing rate were:
    - Average Math Score 79.0% with a 75% passing rate
    - Average Reading Score 81.9% with a 86% passing rate
    - Overall passing rate of 80%
- The top 5 schools in overall passing % were:
    1. Cabrera High School
    2. Thomas High School
    3. Pena High School
    4. Griffin High School
    5. Wilson High School
- The bottom 5 schools in overal passing % were:
    15. Rodriguez High School
    14. Figueroa High School
    13. Huang High School
    12. Johnson High School
    11. Ford High School
    
## Challenge Overview
The grades of the ninth graders at Thomas High School have changed. While administrators do not know the full extent of this academic dishonesty, they want to uphold the standards of state testing and need my help. I will need to remove the ninth-grade math and reading scores from Thomas High School. 

## Challenge Summary
The analysis of results after the reading and math scores were taken out for the 9th graders at Thomas High School were:
- The district summary was affected by:
    - Average Math Score went from 79.0% to 78.9% and the passing % went down from 75% to 74%.
    - Average Reading Score slightly changed by hundredths of a percentage and stayed at 81.9% when rounded up and the passing % went         down from 86% to 85%
    - The overall passing percentage went down from 80% to 79%
- In the school summary, the other 14 schools were not affected at all by the removal of scores for Thomas High School.
- While things did not change for the other schools, Thomas High School was drastically affected by the removal of scores.
    - The average math score went from 83.85 to 83.35 with a math passing % going down from 93.27% to 66.91%.
    - The average reading score went from 93.27 to 83.89 wih a reading passing % going down from 97.31% to 80.22%.
    - The overall passing percentage drastically dropped from 95.29% to 68.29%.  This changed them from being the 2nd best overall             performing school to the very last.
- The removal of the 9th-grade scores affected:
    - Math and Reading scores by grade all stayed the same except for now in the 9th grade for Thomas High School value is NaN.
    - Math and Reading scores by school spending slightly changed. While everything else stayed the same, the only changes that happened       were in the spending range between $630-$644. The average Math Score went from 78.52 to 78.50. The average Reading Score went from       81.62 to 81.64.
    - Since Thomas High School is categorized as a Medium Sized School (1000 to 2000 students), the Small and Large sized schools were         not affected. The Average Math Score slightly dropped from 83.37 to 83.36, with the passing % dipping from 93.59% to 88.32%. The         Average Reading Score slight increased from 83.86 to 83.87 but the passing percentage dipped from 96.79% to 91.26%.
    - Since Thomas High School is categorized as a Charter School, District type of schools were not affected at all. Charter Schools         had a slight change with Math Scores going from 83.47 to 83.46 with a pass percentage going down from 93.62% to 90.33%.  Reading         Scores went slightly up from 83.89 to 83.90 but the pass percentage dipped from 96.59% to 93.13%.
