SELECT count(tmp.id) usercount,tmp.create_time
        FROM 
            (SELECT date_format(create_time,'yyyy-MM-dd')as create_time, id
            FROM `banda-etl-s3`.t_customer ) tmp   
        GROUP BY  tmp.create_time
        having tmp.create_time>  '2021-01-01'
        order by tmp.create_time desc