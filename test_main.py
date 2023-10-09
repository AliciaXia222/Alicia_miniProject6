"""
Test goes here

"""

import subprocess


def test_extract():
    """tests extract()"""
    result = subprocess.run(
        ["python", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


# def test_transform_load():
#     """tests transfrom_load"""
#     result = subprocess.run(
#         ["python", "main.py", "transform_load"],
#         capture_output=True,
#         text=True,
#         check=True,
#     )
#     assert result.returncode == 0
#     assert "Transforming data..." in result.stdout


# def test_general_query():
#     """tests general_query"""
#     result = subprocess.run(
#         [
#             "python",
#             "main.py",
#             "general_query",
#             """SELECT t2.Performer, t2.Show, COUNT(t2.Show) AS total_show_played
#             FROM default.performerdb t2
#             JOIN default.showdb t1 ON t2.id = t1.id
#             GROUP BY t2.Show
#             ORDER BY total_show_played DESC
#             LIMIT 10""",
#         ],
#         capture_output=True,
#         text=True,
#         check=True,
#     )
#     assert result.returncode == 0


if __name__ == "__main__":
    test_extract()
    # test_transform_load()
    # test_general_query()
