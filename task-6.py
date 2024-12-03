# Write a crud operation to sum EN 96 blocks of all sellers and buyers for current date and of "WR" source 
# and It should pick the max revision always

import pymysql
import json

def get_data():
    try:
      
        db_connection = pymysql.connect(
            host='localhost',
            user='root',
            password='vanshita1234@',
            database='python_training',
        )
        cursor = db_connection.cursor()

       

        
        
        with open("data_set_python_training.json",'r') as file:
            data = json.load(file)

        sum_block_query = """
        SELECT 
            std.id AS id,
            SUM(sbt.block_value) AS total_block_value
        FROM 
            schedule_revision_details AS srt
        INNER JOIN 
            schedule_transaction_details AS std 
            ON srt.id = std.sch_rev_details_id
        INNER JOIN 
            schedule_blockwise_data AS sbt 
            ON std.id = sbt.tran_details_id
        WHERE
            srt.data_date = CURRENT_DATE
            AND srt.source_name = 'MH'
            AND srt.revision_no = (
                SELECT MAX(revision_no) 
                FROM schedule_revision_details 
                WHERE data_date = CURRENT_DATE 
                AND source_name = 'MH'
            )
        GROUP BY 
            std.id;
        """
        cursor.execute(sum_block_query)
        sum_results = cursor.fetchall()

        
        print(f"{sum_results}")

    except Exception as e:
        print(f"Error occurred at line:{e.__traceback__.tb_lineno}")

get_data()
    

    