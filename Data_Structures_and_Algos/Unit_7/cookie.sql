--1) What Publisher is located in GARDEN CITY? 
-- Answer: DOUBLEDAY AND COMPANY INC.
-- Code: INSERT BELOW THIS LINE

select p.publisher,
       p.pcity  
from pub as p
where p.pcity = 'GARDEN CITY'

--2) How many books in the catalogue come from publishers in NEW YORK? 
-- Answer: 33
-- Code: INSERT BELOW THIS LINE

select count(b.accno) 
from bib as b
join pub as p on b.pubid = p.pubid
where p.pcity = 'NEW YORK'


--3) Find the average price of a book in the SOCIAL CHANGE subject category. 
-- Answer: 8.625
-- Code: INSERT BELOW THIS LINE

select avg(b.price) 
from bib as b
inner join indx as i on b.accno = i.accno
inner join sub as s on i.subcode = s.subcode
where s.subject = 'SOCIAL CHANGE'


--4) How many books from SAN FRANCISCO publishers are about UNIVERSITIES AND COLLEGES? 
-- Answer: 2
-- Code: INSERT BELOW THIS LINE

select count(b.accno)
from bib as b
join indx as i on b.accno = i.accno
join sub as s on i.subcode = s.subcode
join pub as p on b.pubid = p.pubid
where p.pcity = 'SAN FRANCISCO' and s.subject = 'UNIVERSITIES AND COLLEGES'


--5) Books in which subject category have the highest price? 
-- Answer: COMMUNICATION - ECONOMIC ASPECTS, and COMMUNICATION POLICY - US
-- Code: INSERT BELOW THIS LINE

select s.subcode, s.subject, sub_s.avg_price as max_avg_price from sub as s
join (select s.subcode, avg(b.price) avg_price
    from bib as b
    inner join indx as i on b.accno = i.accno
    inner join sub as s on i.subcode = s.subcode
    group by s.subcode) as sub_s
on sub_s.subcode = s.subcode

where sub_s.avg_price = (
    select max(avg_price) from (
    select s.subcode, avg(b.price) avg_price
        from bib as b
        inner join indx as i on b.accno = i.accno
        inner join sub as s on i.subcode = s.subcode
        group by s.subcode))

order by sub_s.avg_price desc

--6) Among books costing 15 US$ or more, which publisher ranks highest in terms of average book HEIGHT? 
-- Answer: DIABLO PRESS
-- Code: INSERT BELOW THIS LINE

select p.pubid, p.publisher, sub_p.avg_height from pub as p
join  ( select p.pubid, avg(b.height) as avg_height
        from bib as b
        join indx as i on b.accno = i.accno
        join sub as s on i.subcode = s.subcode
        join pub as p on b.pubid = p.pubid
        where b.price >= 15
        group by p.pubid) as sub_p
on  p.pubid = sub_p.pubid
where sub_p.avg_height = (  select max(avg_height) from (
                            select p.pubid, avg(b.height) as avg_height
                            from bib as b
                            join indx as i on b.accno = i.accno
                            join sub as s on i.subcode = s.subcode
                            join pub as p on b.pubid = p.pubid
                            where b.price >= 15
                            group by p.pubid))

