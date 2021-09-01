SELECT count(tmp.id) issuecount,tmp.create_time
    FROM 
        (SELECT date_format(create_time,'yyyy-MM-dd')as create_time, id
        FROM `banda-etl-s3`.t_loan_issue  ) tmp
    GROUP BY  tmp.create_time
    having tmp.create_time>  '2020-12-01'
    order by tmp.create_time desc