import unittest

from database import dbase
import result

class TestDbase(unittest.TestCase):
    def test_1(self):
        db = dbase()
        r = db.run_line('create_table table1 (key string, value int)')
        self.assertIsInstance(r,result.success)

        r = db.run_line('insert table1 (key "face", value 3)')
        self.assertIsInstance(r,result.success)

        r = db.run_line('insert table1 (value 4, key "toe")')
        self.assertIsInstance(r,result.success)

        r = db.run_line('insert table1 (key "your mum", value 5)')
        self.assertIsInstance(r,result.success)

        r = db.run_line('select table1 (key = "face")')
        self.assertTrue(isinstance(r, result.select))
        self.assertTrue(len(r.rows)==1)
        self.assertTrue(('face',3) in r.rows)

        r = db.run_line('select table1 (key != "lol")')
        self.assertTrue(isinstance(r, result.select))
        self.assertTrue(len(r.rows)==3)
        self.assertTrue(('face',3) in r.rows)
        self.assertTrue(('your mum',5) in r.rows)
        self.assertTrue(('toe', 4) in r.rows)

        r = db.run_line('select table1 ((key != "face") && (key != "lol"))')
        self.assertTrue(isinstance(r, result.select))
        self.assertTrue(len(r.rows)==2)
        self.assertTrue(('toe',4) in r.rows)
        self.assertTrue(('your mum', 5) in r.rows)


if __name__ == '__main__':
    unittest.main()

