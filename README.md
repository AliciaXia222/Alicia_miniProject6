[![CI](https://github.com/nogibjj/Alicia_miniProject5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Alicia_miniProject5/actions/workflows/cicd.yml)
## Mini Project 6

### Goal:

* Use Copilot to support me writing the code.
* Connect codespace with cloud database "databricks" to enpower the local computer's limitation.
* Write advanced SQL query to mulnipulate data and solve the complicated problem

### Advanced Query:

<img width="605" alt="Screenshot 2023-10-08 at 9 50 55 PM" src="https://github.com/nogibjj/IDS706_Alicia_miniproject4/assets/143651934/dad03812-b676-415c-ab80-65933ea3d1b4">

* Dictionary:

Performer: The name of the actor, according to IMDb.
Show: The television show where this actor appeared in more than half the episodes
Score_per_year: #LEAD + #Shows + 0.25*(#SUPPORT) / "Years Since"

The query retrieves data from two tables (default.performerdb and default.showdb), performs an inner join based on the id column, calculates the count for each type of shows being played, orders the results by total_shows_played in descending order, and limits the output to the top 10 rows. This query can help identify the most played shows.


#### Here is my .lib file

I seperated the query into 3 parts saved seperatedly in .lib files to help me do CRUD wth SQL automatically with Makefile.

* extract.py

<img width="666" alt="Screenshot 2023-10-08 at 10 03 51 PM" src="https://github.com/nogibjj/IDS706_Alicia_miniproject4/assets/143651934/26fcac6e-1905-4612-acf2-ac1a13941e0b">

* query.py

<img width="361" alt="Screenshot 2023-10-08 at 10 05 06 PM" src="https://github.com/nogibjj/IDS706_Alicia_miniproject4/assets/143651934/da2be775-215e-49e8-af71-b2a270238951">

* transform_load.py

<img width="567" alt="Screenshot 2023-10-08 at 10 06 28 PM" src="https://github.com/nogibjj/IDS706_Alicia_miniproject4/assets/143651934/244b94a2-9819-4a97-842f-cce1bd8f71f8">
