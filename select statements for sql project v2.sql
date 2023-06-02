select student_id
  from students;

select survey_id
  from students
  left outer join survey
  on students.student_id = survey.student_id
  where student_name = "insert student name" and survey_id not null
  order by students.student_id;

select company_name
  from company;

select tag_name
  from tag;

insert into survey (survey_id, student_id)
  values("insert int value", "insert int value");

update survey
  set student_id = (4194039)
  where survey_id = (1.675);

insert into tag(tag_name, specialization)
  values('new tag name', 'new specialization');

insert into company(EIN, department, location, phone_number, company_name)
  values(new EIN, 'new department', 'new location',
  new phone number, 'new company name');

create view submission_data as
  select survey_id, internship_name, company_name, ID, student_name
    from students, company, survey
    where survey_id not null
    group by ID, survey_id;


UPDATE survey
SET survey_id = 1.652
WHERE student_id = "insert int id";


DELETE FROM survey
WHERE student_id is null;