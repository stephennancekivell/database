import unittest

from database import dbase

class TestDbase(unittest.TestCase):
    def test_1(self):
        db = dbase()
        db.run_line('create_table table1 (key string, value int)')
        db.run_line('insert table1 (key "face", value 3)')
        db.run_line('insert table1 (value 4, key "toe")')
        db.run_line('insert table1 (key "your mum", value 5)')
        db.run_line('select table1 (key = "face")')
        db.run_line('select table1 (key != "lol")')
        db.run_line('select table1 ((key != "face") && (key != "lol"))')

if __name__ == '__main__':
    unittest.main()

